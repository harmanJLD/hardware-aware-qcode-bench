from qiskit import QuantumCircuit
import numpy as np

# Define the number of qubits
num_qubits = 5

# Create a QuantumCircuit
qc = QuantumCircuit(num_qubits)

# Define the angles for the rotation layers
ry_angles_1 = [0.1, 0.2, 0.3, 0.4, 0.5]
ry_angles_2 = [0.6, 0.7, 0.8, 0.9, 1.0]

# First RY rotation layer
for i in range(num_qubits):
    qc.ry(ry_angles_1[i], i)

# Circular CX entanglement layer
for i in range(num_qubits - 1):
    qc.cx(i, i + 1)
qc.cx(num_qubits - 1, 0)

# Second RY rotation layer
for i in range(num_qubits):
    qc.ry(ry_angles_2[i], i)