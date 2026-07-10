from qiskit import QuantumCircuit
import math

qc = QuantumCircuit(4)

# Initial Hadamards on all qubits
for i in range(4):
    qc.h(i)

# Cost layer with gamma = 0.8
gamma = 0.8
edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
for edge in edges:
    qc.rzz(2 * gamma, edge[0], edge[1])

# Mixer layer with beta = 0.4
beta = 0.4
for i in range(4):
    qc.rx(2 * beta, i)