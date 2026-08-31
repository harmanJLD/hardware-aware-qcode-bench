# hardware-aware-qcode-bench

A reproducible benchmark for evaluating LLM-generated quantum code along two axes:
functional correctness under noiseless simulation, and hardware executability after
compilation to a target device model.

Existing quantum code benchmarks score generated circuits on simulated output
equivalence alone. That criterion is necessary but insufficient: a circuit that is
exactly correct in simulation may inflate in depth and gate count after transpilation
to a native gate set and coupling map, to the point where decoherence dominates. This
benchmark quantifies that discrepancy, referred to throughout as the
simulation-to-hardware gap.

---

## Paper

**Hardware-Aware Correctness Benchmarking for LLM-Generated Quantum Code**
Harmandeep Kaur. Q-GenAI Workshop, IEEE International Conference on Quantum Computing
and Engineering (QCE) 2026, Toronto.

[Camera-ready PDF](paper.pdf)

© 2026 IEEE. Personal use of this material is permitted. Permission from IEEE must be
obtained for all other uses, in any current or future media, including reprinting or
republishing this material for advertising or promotional purposes, creating new
collective works, for resale or redistribution to servers or lists, or reuse of any
copyrighted component of this work in other works.

---

## Overview

The benchmark evaluates a language model's quantum code output in two stages.
Generated code is first executed in a sandbox and checked against a machine-verifiable
reference under noiseless simulation. Circuits are then transpiled to each target
backend and characterized by structural and noise-derived metrics.

The framework is deliberately device-free. All hardware metrics derive from
transpilation and published calibration data rather than device execution, so the
benchmark is reproducible at no cost and without queue access.

---

## Metrics

### Axis 1: functional correctness

| Metric | Definition |
| --- | --- |
| `C` | Compile rate. Fraction of generations that parse and construct a Qiskit circuit without runtime error. |
| `F` | Functional pass rate. Fraction satisfying the task reference check under noiseless simulation. |
| `pass@k` | Standard pass@k over k samples per task. |

Statevector checks require fidelity ≥ 0.99 up to global phase. Expectation-value
checks use a tolerance of 1e-4.

### Axis 2: hardware executability

| Metric | Definition |
| --- | --- |
| `G` | Native-gate compliance. Fraction of pre-transpilation gates already in the target basis. |
| `V` | Connectivity violations. Two-qubit interactions infeasible under the trivial layout. |
| `D` | Depth inflation. Post- to pre-transpilation depth ratio. |
| `T` | Two-qubit overhead. Post- to pre-transpilation two-qubit gate count ratio. |
| `ESP` | Estimated success probability. Product of per-operation success probabilities over the transpiled circuit, from the backend's reported error rates. |

### Derived quantities

`F_H(tau)` is the hardware-conditioned pass rate: the fraction of generations that are
functionally correct and achieve `ESP >= tau` on target `H`. The simulation-to-hardware
gap is `Delta_H(tau) = F - F_H(tau)`.

Because `Delta_H` is bounded above by `F`, it partly rewards weak generators. Two fairer
comparators are also reported: the conditional failure rate among functionally correct
circuits, and relative efficiency, defined as `ESP_generated / ESP_reference` against an
expert reference solution transpiled identically.

**Note on ESP.** ESP is an analytic quantity derived from calibration snapshots. It is
neither a measured device output nor a noisy simulation, and should be read as a
relative proxy for device viability rather than a predicted hardware result.

---

## Task suite

Sixteen natural-language prompts with explicit qubit counts and machine-checkable
references, defined in `tasks.py`.

**State preparation (6).** Bell, GHZ-4, GHZ-8, W-3, uniform superposition, basis-state
encoding. Reference is the target statevector up to global phase.

**Canonical algorithms (6).** Four-qubit QFT checked by unitary equivalence, one Grover
iteration, phase-oracle Bernstein-Vazirani and Deutsch-Jozsa, textbook phase estimation
of the T gate, and the SWAP test.

**Variational workloads (4).** A fully specified hardware-efficient ansatz, a depth-1
QAOA MaxCut circuit on the 4-ring checked by cost-observable expectation, a first-order
Trotter step, and a two-local circular-entanglement ansatz.

---

## Target backends

Two backend models were selected to span the topology and gate-basis extremes of current
NISQ platforms.

| Target | Description | Basis |
| --- | --- | --- |
| `FakeTorino` | 133-qubit IBM Heron model, heavy-hex connectivity, published calibration data | CZ, RZ, SX, X |
| Ion-style model | Synthetic 25-qubit `GenericBackendV2` (seed 42), all-to-all connectivity, uniform seeded error rates | RXX, RZ, RX, RY |

The ion-style target is a topology and basis contrast, not a calibrated vendor device.
Cross-target comparisons therefore reflect error-rate assumptions in addition to
architecture.

---

## Released results

Five models were evaluated on 10 July 2026 through a unified API gateway: Gemini 2.5
Pro, Claude Sonnet 4.5, GPT-4o, DeepSeek-V3, and Qwen2.5-Coder-32B-Instruct. Each
received identical prompts and a system instruction to return only Qiskit code, with a
single attempt and no repair loop. 399 of 400 generations completed.

At `tau = 0.9` on the ion-style target, the four frontier models lose between 26 and 39
percentage points relative to their functional pass rates, a mean simulation-to-hardware
gap of 33.6 points. Among functionally correct circuits, 39 to 46 percent fall below the
threshold, and this conditional failure rate is comparable across all four.

On the calibrated heavy-hex target, every functionally correct generation clears
`tau = 0.9`, and the binary metric only begins to separate models at `tau >= 0.95`.
Hardware-conditioned pass rates should therefore be reported as threshold curves rather
than single numbers, with the continuous metrics doing the discriminating where the
binary metric saturates.

Raw model outputs are in `generations/`. Running `run_eval.py` regenerates the
per-generation metrics table as `results.csv`.

---

## Installation

Python 3.10 or later.

```bash
python -m venv qenv && source qenv/bin/activate
pip install qiskit qiskit-aer qiskit-ibm-runtime openai anthropic google-genai
```

Provider API keys are read from the environment. Set only those required for the models
listed in `MODELS`.

---

## Usage

Configure the target models in `MODELS` in `generate.py`, then:

```bash
python generate.py    # samples k generations per task per model
python run_eval.py    # executes, checks, transpiles, and aggregates
```

`run_eval.py` prints the aggregate results table and writes per-generation metrics to
`results.csv`.

Default configuration: `k = 5` samples per task, temperature 0.8,
`optimization_level = 3`, `seed_transpiler = 11` (SABRE routing).

---

## Repository layout

```
tasks.py         Sixteen task specifications with reference checks
harness.py       Sandboxed execution, checking, transpilation, metrics
generate.py      Model sampling
run_eval.py      Aggregation and results table
generations/     Raw model outputs
paper.pdf        QCE26 camera-ready
```

---

## Limitations

Stated in full in Section VI of the paper. The principal ones:

1. ESP is an analytic estimate from calibration snapshots rather than a device run, and
   the ion-style target uses synthetic uniform error rates.
2. Prompts specify the task only, not the target basis, coupling map, or an optimization
   objective. The benchmark therefore measures how well generic Qiskit output survives
   compilation, not whether a model can be directed to produce hardware-aware code.
3. The suite emphasizes small and mid-sized circuits where exact reference checking is
   tractable, which is the same regime in which the heavy-hex metric saturates.
4. Evaluation is single-shot, whereas deployed assistants iterate against compiler
   feedback.
5. Bootstrap intervals resample generations without modelling the clustering of the k
   samples drawn per task, and are consequently narrower than a task-clustered estimate.
6. Relative efficiency is normalized against one expert reference per task, which is a
   strong but not provably optimal circuit.
7. Functional checks compare final states, unitaries, or single expectation values, so a
   circuit reaching the reference output by an unintended route is scored correct.

---

## Contributing

Contributions are welcome, particularly additional target backends, expanded task
coverage, target-conditioned prompting variants, and repair-loop evaluation. Please open
an issue before submitting substantial changes so that metric definitions remain
consistent with the released results.

---

## Citation

```bibtex
@inproceedings{kaur2026hardware,
  title     = {Hardware-Aware Correctness Benchmarking for {LLM}-Generated Quantum Code},
  author    = {Kaur, Harmandeep},
  booktitle = {IEEE International Conference on Quantum Computing and Engineering (QCE),
               Q-GenAI Workshop},
  year      = {2026}
}
```
