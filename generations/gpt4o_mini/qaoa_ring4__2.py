from qiskit import QuantumCircuit
import numpy as np

# Parameters
gamma = 0.8
beta = 0.4

# Create a QuantumCircuit with 4 qubits
qc = QuantumCircuit(4)

# Initial Hadamard gates
qc.h([0, 1, 2, 3])

# Cost layer for edges (0,1), (1,2), (2,3), (3,0)
qc.rzz(2 * gamma, 0, 1)  # Edge (0, 1)
qc.rzz(2 * gamma, 1, 2)  # Edge (1, 2)
qc.rzz(2 * gamma, 2, 3)  # Edge (2, 3)
qc.rzz(2 * gamma, 3, 0)  # Edge (3, 0)

# Mixer layer
qc.rx(2 * beta, [0, 1, 2, 3])