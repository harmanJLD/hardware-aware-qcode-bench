from qiskit import QuantumCircuit
from qiskit.circuit.library import RZZGate, RXGate
import numpy as np

# Define parameters
gamma = 0.8
beta = 0.4

# Create a quantum circuit with 4 qubits
qc = QuantumCircuit(4)

# Apply Hadamard gates to all qubits
qc.h(range(4))

# Cost layer: Apply RZZ gates for each edge in the graph
edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
for edge in edges:
    qc.append(RZZGate(2 * gamma), edge)

# Mixer layer: Apply RX gates to all qubits
for qubit in range(4):
    qc.rx(2 * beta, qubit)