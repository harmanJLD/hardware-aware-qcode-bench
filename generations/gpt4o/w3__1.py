from qiskit import QuantumCircuit
from math import sqrt

qc = QuantumCircuit(3)

# Create the W state
qc.ry(2 * acos(sqrt(1/3)), 0)
qc.cx(0, 1)
qc.ry(2 * acos(sqrt(1/2)), 1)
qc.cx(1, 2)
qc.ry(2 * acos(sqrt(0)), 2)
qc.cx(0, 2)

# The circuit 'qc' now prepares the 3-qubit W state