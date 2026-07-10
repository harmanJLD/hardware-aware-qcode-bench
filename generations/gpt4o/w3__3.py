from qiskit import QuantumCircuit
from qiskit.circuit.library import RYGate, RZZGate

# Initialize a 3-qubit quantum circuit
qc = QuantumCircuit(3)

# Apply RY gate on qubit 0 to create a superposition of |0> and |1>
qc.ry(2 * (1.2309594173407747), 0)

# Use a controlled RY gate (decomposed into RY and CNOTs) to entangle qubit 1
qc.cry(2 * (1.9106332362490186), 0, 1)

# Use a controlled RY gate to entangle qubit 2
qc.cry(2 * (0.33983690945412187), 1, 2)

# Add RZZ Gate to adjust phases between amplitudes
qc.rzz(-0.33983690945412187, 0, 1)

# Add RZZ Gate to adjust phases between amplitudes
qc.rzz(-0.33983690945412187, 1, 2)

# The circuit is now configured to prepare the W state