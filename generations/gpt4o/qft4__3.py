from qiskit import QuantumCircuit
from math import pi

# Define the quantum circuit with 4 qubits
qc = QuantumCircuit(4)

# Apply the Hadamard gate and controlled phase gates for QFT
qc.h(0)
qc.cp(pi/2, 1, 0)
qc.cp(pi/4, 2, 0)
qc.cp(pi/8, 3, 0)

qc.h(1)
qc.cp(pi/2, 2, 1)
qc.cp(pi/4, 3, 1)

qc.h(2)
qc.cp(pi/2, 3, 2)

qc.h(3)

# Swap the qubits to reverse the order them
qc.swap(0, 3)
qc.swap(1, 2)