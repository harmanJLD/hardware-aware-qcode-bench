from qiskit import QuantumCircuit
from math import sqrt

qc = QuantumCircuit(3)

# Apply a sequence of gates to prepare the W state
qc.ry(2 * acos(sqrt(1/3)), 2)
qc.cx(2, 1)
qc.cry(2 * acos(sqrt(1/2)), 1, 0)
qc.cx(1, 0)
qc.x(2)