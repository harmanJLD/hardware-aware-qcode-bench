import numpy as np
from qiskit.circuit import QuantumCircuit

# Define the number of qubits
num_qubits = 5

# Define the angles for the rotation layers
ry_params1 = [0.1, 0.2, 0.3, 0.4, 0.5]
ry_params2 = [0.6, 0.7, 0.8, 0.9, 1.0]

# Create a QuantumCircuit object
qc = QuantumCircuit(num_qubits)

# First RY rotation layer
for i in range(num_qubits):
    qc.ry(ry_params1[i], i)

# Circular CX entanglement layer
for i in range(num_qubits - 1):
    qc.cx(i, i + 1)
qc.cx(num_qubits - 1, 0)

# Second RY rotation layer
for i in range(num_qubits):
    qc.ry(ry_params2[i], i)