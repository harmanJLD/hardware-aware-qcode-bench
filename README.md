# Hardware-Aware Correctness Benchmark: Run Protocol

Deadline-day protocol for QCE26 submission 1591. Total wall time roughly 3-4 hours,
most of it LLM API calls.

## Setup (10 min)

    python -m venv qenv && source qenv/bin/activate
    pip install qiskit qiskit-aer qiskit-ibm-runtime openai anthropic google-genai

## Experiment 1: main evaluation (the paper's Table 1)

Design, fixed and verified:
- Tasks: 16 prompts (6 state preparation, 6 canonical algorithms, 4 variational),
  defined in tasks.py with machine-checkable references. All references verified to
  pass their own checks.
- Sampling: k = 5 per task per model, temperature 0.8. Report pass@1 (mean over
  samples) and optionally pass@5.
- Backends: FakeTorino (133-qubit IBM Heron model, heavy-hex, {cz, rz, sx, x} basis)
  and a 25-qubit all-to-all trapped-ion-style model ({rxx, rz, rx, ry} basis,
  GenericBackendV2 seed 42).
- Transpilation: Qiskit optimization_level=3, seed_transpiler=11 (SABRE routing).
- Noise-aware fidelity: ESP = product of (1 - gate error) over post-transpilation
  operations using backend calibration data. Hardware pass threshold tau = 0.5.

Steps:
1. Edit MODELS in generate.py to the models you have API keys for. Aim for 4-6:
   e.g. gpt-4o, claude-sonnet-4-5, gemini-2.5-pro, plus 1-3 open-weight coder models
   through an OpenAI-compatible endpoint. Record access dates for the paper.
2. Run: python generate.py     (16 tasks x 5 samples x M models; ~10-20 min per model)
3. Run: python run_eval.py     (prints Table 1: C, F, F_hex, F_ion, Delta_hex;
   writes per-generation results.csv)

Paper mapping: Table 1 comes straight from the aggregate printout. N=16, k=5, K=2,
tau=0.5, optimization level 3. The Delta_hex column is the headline
simulation-to-hardware gap.

## Experiment 2: failure-mode decomposition (Section V-B)

No new runs needed; everything is in results.csv. Slice it four ways:
1. Idealized gate usage: mean hex_native_compliance per model; correlate low
   compliance with high hex_2q_overhead.
2. Connectivity-blind structure: hex_conn_violations for the ion-friendly tasks
   (ghz8, qaoa_ring4, twolocal5 have long-range or ring interactions).
3. Depth-inefficient constructions: distribution of hex_depth_inflation per task
   category (box plot = the paper's Figure 1 candidate).
4. Topology sensitivity: compare Delta_hex vs Delta_ion. If the gap shrinks on the
   all-to-all target, connectivity (not gate basis) dominates, which is the
   cleanest causal claim in the paper.

## Experiment 3 (optional, if time permits): relative efficiency

For each functionally correct generation, compute ESP(generated)/ESP(reference).
Reference ESPs are already computable from tasks.py; this normalizes away task
difficulty and isolates model inefficiency. One extra paragraph in Section V-C.

## Figure 1

Scatter of F (x-axis) vs F_hex (y-axis), one point per model, diagonal line.
Points below the diagonal visualize the gap. ~10 lines of matplotlib from the
aggregate table.

## Reference ESP values (from smoke test, for sanity checking)

Task ESPs on heavy-hex range 0.94 (qft4) to 0.999 (basis5); on the ion model,
qft4 = 0.69 and qpe_t = 0.69 are the hardest. All references clear tau = 0.5,
so any hardware failures observed are attributable to generation quality.

## Honesty notes for the paper

- The ion backend is a synthetic GenericBackendV2 with seeded error rates, not a
  vendor calibration snapshot. Say "trapped-ion-style all-to-all topology model"
  in the paper, not "IonQ device". Alternatively, override its Target error rates
  with published IonQ Forte numbers and cite them.
- ESP is an analytic proxy, not a device run. The draft's Limitations section
  already covers this; keep it.
- Release this directory (tasks.py, harness.py, generate.py, run_eval.py,
  generations/, results.csv) as the public benchmark repo the abstract promises.
