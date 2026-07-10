"""Task suite: 16 prompts across state preparation, algorithms, variational workloads.
Each task: id, category, n_qubits, prompt, check type, and a reference builder.
Check types:
  state   -> statevector fidelity vs reference >= 0.99
  unitary -> Operator equivalence up to global phase
  expval  -> expectation of observable within tol of reference
"""
import numpy as np
from qiskit import QuantumCircuit
from qiskit.circuit.library import QFT
from qiskit.quantum_info import SparsePauliOp

FID_THRESHOLD = 0.99

# ---------- reference circuits ----------

def ref_bell():
    qc = QuantumCircuit(2); qc.h(0); qc.cx(0, 1); return qc

def ref_ghz(n):
    qc = QuantumCircuit(n); qc.h(0)
    for i in range(n - 1): qc.cx(i, i + 1)
    return qc

def ref_w3():
    qc = QuantumCircuit(3)
    qc.ry(2 * np.arccos(1 / np.sqrt(3)), 0)
    qc.ch(0, 1)
    qc.cx(1, 2)
    qc.cx(0, 1)
    qc.x(0)
    return qc

def ref_uniform5():
    qc = QuantumCircuit(5); qc.h(range(5)); return qc

def ref_basis():
    qc = QuantumCircuit(5); qc.x([1, 2, 4]); return qc

def ref_qft4():
    return QFT(4, do_swaps=True)

def ref_grover3():
    qc = QuantumCircuit(3)
    qc.h(range(3))
    # oracle for state with q0=1, q1=0, q2=1
    qc.x(1); qc.h(2); qc.ccx(0, 1, 2); qc.h(2); qc.x(1)
    # diffuser
    qc.h(range(3)); qc.x(range(3))
    qc.h(2); qc.ccx(0, 1, 2); qc.h(2)
    qc.x(range(3)); qc.h(range(3))
    return qc

def ref_bv():
    qc = QuantumCircuit(4)
    qc.h(range(4))
    for q in (0, 1, 3): qc.z(q)   # s = (s0,s1,s2,s3) = (1,1,0,1)
    qc.h(range(4))
    return qc

def ref_dj():
    qc = QuantumCircuit(3)
    qc.h(range(3))
    qc.z(0); qc.z(1)              # phase oracle for f(x) = x0 XOR x1
    qc.h(range(3))
    return qc

def ref_qpe():
    qc = QuantumCircuit(4)
    qc.x(3)
    qc.h([0, 1, 2])
    for j, q in enumerate([0, 1, 2]):
        qc.cp(np.pi / 4 * (2 ** j), q, 3)
    qc.compose(QFT(3, do_swaps=True).inverse(), qubits=[0, 1, 2], inplace=True)
    return qc

def ref_swaptest():
    qc = QuantumCircuit(3)
    qc.x(1); qc.h(2)
    qc.h(0); qc.cswap(0, 1, 2); qc.h(0)
    return qc

def ref_hea():
    angles = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
    qc = QuantumCircuit(4)
    for rep in range(2):
        for i in range(4): qc.ry(angles[rep * 4 + i], i)
        for i in range(3): qc.cx(i, i + 1)
    return qc

def ref_qaoa():
    qc = QuantumCircuit(4)
    qc.h(range(4))
    for (a, b) in [(0, 1), (1, 2), (2, 3), (3, 0)]: qc.rzz(1.6, a, b)
    for q in range(4): qc.rx(0.8, q)
    return qc

QAOA_OBS = SparsePauliOp(["IIZZ", "IZZI", "ZZII", "ZIIZ"])

def ref_trotter():
    qc = QuantumCircuit(3)
    qc.rzz(1.0, 0, 1); qc.rzz(1.0, 1, 2)
    for q in range(3): qc.rx(1.0, q)
    return qc

def ref_twolocal5():
    qc = QuantumCircuit(5)
    for i in range(5): qc.ry(0.1 * (i + 1), i)
    for (a, b) in [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]: qc.cx(a, b)
    for i in range(5): qc.ry(0.1 * (i + 6), i)
    return qc

# ---------- task definitions ----------

STYLE = ("Use Qiskit 2.x. Write Python code that defines a QuantumCircuit object "
         "named qc. Do not add measurements. Do not simulate or print anything. "
         "Return only code.")

TASKS = [
    # --- state preparation ---
    dict(id="bell", category="state_prep", n=2, check="state", ref=ref_bell,
         prompt="Prepare a Bell state (|00> + |11>)/sqrt(2) on 2 qubits."),
    dict(id="ghz4", category="state_prep", n=4, check="state", ref=lambda: ref_ghz(4),
         prompt="Prepare a 4-qubit GHZ state (|0000> + |1111>)/sqrt(2)."),
    dict(id="ghz8", category="state_prep", n=8, check="state", ref=lambda: ref_ghz(8),
         prompt="Prepare an 8-qubit GHZ state (|0...0> + |1...1>)/sqrt(2)."),
    dict(id="w3", category="state_prep", n=3, check="state", ref=ref_w3,
         prompt="Prepare the 3-qubit W state (|001> + |010> + |100>)/sqrt(3)."),
    dict(id="uniform5", category="state_prep", n=5, check="state", ref=ref_uniform5,
         prompt="Prepare the uniform superposition over all 32 computational basis states on 5 qubits."),
    dict(id="basis5", category="state_prep", n=5, check="state", ref=ref_basis,
         prompt="On 5 qubits, prepare the computational basis state in which qubits 1, 2, and 4 are |1> and qubits 0 and 3 are |0>."),

    # --- canonical algorithms ---
    dict(id="qft4", category="algorithm", n=4, check="unitary", ref=ref_qft4,
         prompt="Implement the 4-qubit quantum Fourier transform, including the final qubit-reversal SWAP gates. Qubit 0 is the least significant qubit."),
    dict(id="grover3", category="algorithm", n=3, check="state", ref=ref_grover3,
         prompt="Implement one full iteration of Grover's algorithm on 3 qubits (initial Hadamards, phase oracle, diffuser). The marked computational basis state has qubit 0 = 1, qubit 1 = 0, qubit 2 = 1."),
    dict(id="bv4", category="algorithm", n=4, check="state", ref=ref_bv,
         prompt="Implement the Bernstein-Vazirani algorithm on 4 qubits using the phase-oracle formulation (no ancilla qubit): apply Hadamards to all qubits, apply the phase oracle |x> -> (-1)^(s.x)|x> for the secret string with s_0=1, s_1=1, s_2=0, s_3=1 (s_i is the bit associated with qubit i), then apply Hadamards to all qubits."),
    dict(id="dj3", category="algorithm", n=3, check="state", ref=ref_dj,
         prompt="Implement the Deutsch-Jozsa algorithm on 3 qubits using the phase-oracle formulation (no ancilla): Hadamards on all qubits, the phase oracle |x> -> (-1)^(f(x))|x> for the balanced function f(x) = x_0 XOR x_1 (x_i is the value of qubit i), then Hadamards on all qubits."),
    dict(id="qpe_t", category="algorithm", n=4, check="state", ref=ref_qpe,
         prompt="Implement textbook quantum phase estimation with 3 counting qubits (qubits 0-2, qubit 0 least significant) estimating the phase of the T gate applied to qubit 3, with qubit 3 prepared in the eigenstate |1>. Use controlled-phase gates for the controlled powers of T and finish with the inverse QFT (including its SWAP gates) on the counting register. Do not measure."),
    dict(id="swaptest", category="algorithm", n=3, check="state", ref=ref_swaptest,
         prompt="Implement the SWAP test on 3 qubits: qubit 0 is the ancilla, qubit 1 is prepared in |1>, qubit 2 is prepared in |+> = H|0>. Apply H to the ancilla, a controlled-SWAP of qubits 1 and 2 controlled on the ancilla, then H on the ancilla. Do not measure."),

    # --- variational / application ---
    dict(id="hea4", category="variational", n=4, check="state", ref=ref_hea,
         prompt="Build a hardware-efficient ansatz on 4 qubits with exactly 2 layers. Each layer applies RY(theta) to every qubit followed by CX(0,1), CX(1,2), CX(2,3). The RY angles in order of application are 0.1, 0.2, 0.3, 0.4 (layer 1, qubits 0-3) and 0.5, 0.6, 0.7, 0.8 (layer 2, qubits 0-3)."),
    dict(id="qaoa_ring4", category="variational", n=4, check="expval", ref=ref_qaoa,
         obs=QAOA_OBS, tol=1e-4,
         prompt="Build a depth-1 QAOA circuit for MaxCut on the 4-node ring graph with edges (0,1), (1,2), (2,3), (3,0). Start with Hadamards on all 4 qubits. Apply the cost layer exp(-i*gamma*Z_a*Z_b) for each edge as RZZ(2*gamma) with gamma = 0.8, in the edge order given. Then apply the mixer RX(2*beta) with beta = 0.4 to every qubit."),
    dict(id="trotter3", category="variational", n=3, check="state", ref=ref_trotter,
         prompt="Starting from |000> on 3 qubits, apply a single first-order Trotter step: RZZ(1.0) on qubits (0,1), then RZZ(1.0) on qubits (1,2), then RX(1.0) on each of the 3 qubits."),
    dict(id="twolocal5", category="variational", n=5, check="state", ref=ref_twolocal5,
         prompt="Build a two-local ansatz on 5 qubits: first an RY rotation layer with angles 0.1, 0.2, 0.3, 0.4, 0.5 on qubits 0-4, then circular CX entanglement CX(0,1), CX(1,2), CX(2,3), CX(3,4), CX(4,0), then a second RY layer with angles 0.6, 0.7, 0.8, 0.9, 1.0 on qubits 0-4."),
]

def get_task(task_id):
    for t in TASKS:
        if t["id"] == task_id:
            return t
    raise KeyError(task_id)
