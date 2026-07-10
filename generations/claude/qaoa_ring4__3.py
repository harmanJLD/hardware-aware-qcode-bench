from qiskit import QuantumCircuit
import numpy as np

qc = QuantumCircuit(4)

# Initial Hadamards on all qubits
for i in range(4):
    qc.h(i)

# Cost layer parameters
gamma = 0.8

# Apply RZZ gates for each edge in the given order
edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
for a, b in edges:
    qc.rzz(2 * gamma, a, b)

# Mixer layer parameters
beta = 0.4

# Apply RX gates to all qubits
for i in range(4):
    qc.rx(2 * beta, i)