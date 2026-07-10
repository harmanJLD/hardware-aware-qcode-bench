from qiskit import QuantumCircuit
from qiskit.circuit.library import RZZGate, RXGate
import numpy as np

# Parameters
gamma = 0.8
beta = 0.4

# Initialize quantum circuit with 4 qubits
qc = QuantumCircuit(4)

# Apply Hadamard gates to all qubits
qc.h(range(4))

# Apply cost layer for each edge using RZZ gates
edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
for (a, b) in edges:
    qc.append(RZZGate(2 * gamma), [a, b])

# Apply mixer layer RX gates to each qubit
for qubit in range(4):
    qc.rx(2 * beta, qubit)