from qiskit import QuantumCircuit
import math

qc = QuantumCircuit(4)

# QFT on 4 qubits (qubit 0 is LSB)
# Apply QFT gates
for j in range(4):
    qc.h(j)
    for k in range(j + 1, 4):
        qc.cp(math.pi / (2 ** (k - j)), k, j)

# Qubit reversal swaps
qc.swap(0, 3)
qc.swap(1, 2)