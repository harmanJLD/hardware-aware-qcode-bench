"""Evaluation harness.

Pipeline per generation:
  1. Execute generated code in a subprocess sandbox (timeout, no network needed);
     the code must define `qc`. Circuit is passed back via QPY.
  2. Axis 1 (functional): statevector fidelity / unitary equivalence / expectation check.
  3. Axis 2 (hardware): transpile to each backend, compute native-gate compliance,
     connectivity violations, depth inflation, 2q overhead, ESP (noise-aware fidelity),
     and the hardware-conditioned pass flag.
"""
import io, os, subprocess, sys, tempfile
import numpy as np
from qiskit import qpy, transpile
from qiskit.quantum_info import Statevector, Operator
from qiskit.transpiler import CouplingMap
from qiskit.providers.fake_provider import GenericBackendV2
from qiskit_ibm_runtime.fake_provider import FakeTorino

from tasks import FID_THRESHOLD

TAU = 0.5              # ESP floor for hardware-conditioned pass
OPT_LEVEL = 3
SEED_TRANSPILE = 11

RUNNER = r"""
import sys
code = open(sys.argv[1]).read()
ns = {"__name__": "__main__"}
exec(code, ns)
qc = ns.get("qc")
if qc is None:
    raise RuntimeError("generated code did not define `qc`")
from qiskit import qpy
with open(sys.argv[2], "wb") as f:
    qpy.dump(qc, f)
"""

def get_backends():
    hex_backend = FakeTorino()  # 133q Heron, heavy-hex, {cz, rz, sx, x}
    ion_backend = GenericBackendV2(
        num_qubits=25,
        basis_gates=["rxx", "rz", "rx", "ry", "id"],
        coupling_map=CouplingMap.from_full(25),
        seed=42,
    )
    return {"hex": hex_backend, "ion": ion_backend}

# ---------- sandboxed execution ----------

def run_code(code_str, timeout=60):
    """Execute generated code in a subprocess; return (circuit or None, error string)."""
    with tempfile.TemporaryDirectory() as td:
        src, out, run = (os.path.join(td, f) for f in ("gen.py", "circ.qpy", "runner.py"))
        open(src, "w").write(code_str)
        open(run, "w").write(RUNNER)
        try:
            p = subprocess.run([sys.executable, run, src, out],
                               capture_output=True, text=True, timeout=timeout)
        except subprocess.TimeoutExpired:
            return None, "timeout"
        if p.returncode != 0:
            return None, (p.stderr or "unknown error").strip().splitlines()[-1][:300]
        try:
            with open(out, "rb") as f:
                circs = qpy.load(f)
            return circs[0], ""
        except Exception as e:
            return None, f"qpy load failed: {e}"

# ---------- axis 1: functional correctness ----------

def check_functional(qc, task):
    """Return (passed: bool, detail: str). Assumes qc is a QuantumCircuit."""
    try:
        qc = qc.remove_final_measurements(inplace=False)
        if qc.num_qubits != task["n"]:
            return False, f"wrong width {qc.num_qubits}!={task['n']}"
        ref = task["ref"]()
        if task["check"] == "state":
            sv, rv = Statevector(qc), Statevector(ref)
            fid = float(np.abs(np.vdot(rv.data, sv.data)) ** 2)
            return fid >= FID_THRESHOLD, f"fid={fid:.4f}"
        if task["check"] == "unitary":
            ok = Operator(qc).equiv(Operator(ref))
            return bool(ok), "unitary_equiv" if ok else "unitary_mismatch"
        if task["check"] == "expval":
            val = float(Statevector(qc).expectation_value(task["obs"]).real)
            refval = float(Statevector(ref).expectation_value(task["obs"]).real)
            return abs(val - refval) <= task["tol"], f"val={val:.5f} ref={refval:.5f}"
    except Exception as e:
        return False, f"check error: {str(e)[:200]}"
    return False, "unknown check type"

# ---------- axis 2: hardware executability ----------

def _op_counts(circ):
    depth = circ.depth()
    twoq = sum(1 for inst in circ.data
               if inst.operation.num_qubits == 2 and inst.operation.name != "barrier")
    total = sum(1 for inst in circ.data
                if inst.operation.name not in ("barrier", "measure", "delay"))
    return depth, twoq, total

def native_gate_compliance(circ, backend):
    basis = set(backend.operation_names)
    ops = [inst.operation.name for inst in circ.data
           if inst.operation.name not in ("barrier", "measure", "delay")]
    if not ops:
        return 1.0
    return sum(1 for n in ops if n in basis) / len(ops)

def connectivity_violations(circ, backend):
    """2q interactions infeasible under the trivial layout (generated qubit i -> physical i)."""
    edges = set(map(tuple, backend.coupling_map.get_edges())) if backend.coupling_map else None
    if edges is None:
        return 0
    v = 0
    for inst in circ.data:
        if inst.operation.num_qubits == 2 and inst.operation.name != "barrier":
            a, b = (circ.find_bit(q).index for q in inst.qubits)
            if (a, b) not in edges and (b, a) not in edges:
                v += 1
    return v

def esp(circ, backend):
    """Estimated success probability: product of (1 - error) over post-transpilation ops."""
    target = backend.target
    p = 1.0
    for inst in circ.data:
        name = inst.operation.name
        if name in ("barrier", "delay"):
            continue
        qargs = tuple(circ.find_bit(q).index for q in inst.qubits)
        err = 0.0
        try:
            props = target[name].get(qargs)
            if props is not None and props.error is not None:
                err = props.error
        except Exception:
            pass
        p *= max(0.0, 1.0 - err)
    return p

def hw_metrics(qc, backend_name, backend):
    qc = qc.remove_final_measurements(inplace=False)
    d_pre, tq_pre, n_pre = _op_counts(qc)
    row = {
        f"{backend_name}_native_compliance": round(native_gate_compliance(qc, backend), 4),
        f"{backend_name}_conn_violations": connectivity_violations(qc, backend),
    }
    try:
        tqc = transpile(qc, backend=backend, optimization_level=OPT_LEVEL,
                        seed_transpiler=SEED_TRANSPILE)
        d_post, tq_post, n_post = _op_counts(tqc)
        f_hat = esp(tqc, backend)
        row.update({
            f"{backend_name}_depth_pre": d_pre, f"{backend_name}_depth_post": d_post,
            f"{backend_name}_depth_inflation": round(d_post / d_pre, 3) if d_pre else None,
            f"{backend_name}_2q_pre": tq_pre, f"{backend_name}_2q_post": tq_post,
            f"{backend_name}_2q_overhead": round(tq_post / tq_pre, 3) if tq_pre else None,
            f"{backend_name}_esp": round(f_hat, 4),
            f"{backend_name}_hw_pass": f_hat >= TAU,
            f"{backend_name}_transpile_error": "",
        })
    except Exception as e:
        row.update({f"{backend_name}_esp": 0.0, f"{backend_name}_hw_pass": False,
                    f"{backend_name}_transpile_error": str(e)[:200]})
    return row

# ---------- full evaluation of one generation ----------

def evaluate_generation(code_str, task, backends):
    row = {"task": task["id"], "category": task["category"]}
    qc, err = run_code(code_str)
    row["compiled"] = qc is not None
    row["exec_error"] = err
    if qc is None:
        row.update({"functional_pass": False, "detail": ""})
        for bn in backends:
            row[f"{bn}_hw_pass"] = False
            row[f"{bn}_esp"] = 0.0
        return row
    passed, detail = check_functional(qc, task)
    row["functional_pass"] = passed
    row["detail"] = detail
    for bn, b in backends.items():
        row.update(hw_metrics(qc, bn, b))
        # hardware-conditioned pass requires functional pass as well
        row[f"{bn}_hw_pass"] = bool(passed and row.get(f"{bn}_hw_pass", False))
    return row
