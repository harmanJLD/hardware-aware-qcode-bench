from qiskit import QuantumCircuit
from math import sqrt

qc = QuantumCircuit(3)

# Create superposition for the first qubit
qc.u3(2 * sqrt(1/3), 0, 0, 0)

# Apply controlled rotations to entangle other qubits
qc.cry(2 * sqrt(1/2), 0, 1)
qc.cx(1, 2)