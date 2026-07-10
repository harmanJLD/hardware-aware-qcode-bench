from qiskit import QuantumCircuit
from qiskit.circuit.library import QFT

# Create a QuantumCircuit with 4 qubits (3 counting qubits and 1 eigenstate qubit)
qc = QuantumCircuit(4)

# Prepare qubit 3 in the |1> state
qc.x(3)

# Apply Hadamard gates to the counting qubits (0, 1, 2)
qc.h(0)
qc.h(1)
qc.h(2)

# Controlled phase gates for T gate (which has a phase of π/4)
qc.append(qc.t, [3])
qc.cp(2 * (3.14159 / 4), 0, 3)  # T gate to control 0
qc.cp(2 * (3.14159 / 4), 1, 3)  # T gate to control 1
qc.cp(2 * (3.14159 / 4), 2, 3)  # T gate to control 2

# Apply the inverse Quantum Fourier Transform (QFT) to the counting qubits
qc.append(QFT(3, inverse=True), [0, 1, 2])

# SWAP gates for QFT
qc.swap(0, 2)