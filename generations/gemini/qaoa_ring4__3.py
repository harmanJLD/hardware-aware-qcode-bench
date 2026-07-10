import numpy as np
from qiskit import QuantumCircuit

# Define the parameters
gamma = 0.8
beta = 0.4

# Create a QuantumCircuit with 4 qubits
qc = QuantumCircuit(4)

# 1. Initial state: apply Hadamard gates to all qubits
qc.h(range(4))

# 2. Cost layer: apply RZZ gates for each edge
# Edges: (0,1), (1,2), (2,3), (3,0)
qc.rzz(2 * gamma, 0, 1)
qc.rzz(2 * gamma, 1, 2)
qc.rzz(2 * gamma, 2, 3)
qc.rzz(2 * gamma, 3, 0)

# 3. Mixer layer: apply RX gates to all qubits
qc.rx(2 * beta, range(4))