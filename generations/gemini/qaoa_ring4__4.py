import numpy as np
from qiskit.circuit import QuantumCircuit

# Define parameters
gamma = 0.8
beta = 0.4
num_qubits = 4
edges = [(0, 1), (1, 2), (2, 3), (3, 0)]

# Create the QuantumCircuit object
qc = QuantumCircuit(num_qubits)

# 1. Initial state: Apply Hadamard gates to all qubits
qc.h(range(num_qubits))

# 2. Cost layer: Apply RZZ gates for each edge
for u, v in edges:
    qc.rzz(2 * gamma, u, v)

# 3. Mixer layer: Apply RX gates to all qubits
qc.rx(2 * beta, range(num_qubits))