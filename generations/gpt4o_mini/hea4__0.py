from qiskit import QuantumCircuit
import numpy as np

# Define the angles for the RY rotations
angles_layer_1 = [0.1, 0.2, 0.3, 0.4]
angles_layer_2 = [0.5, 0.6, 0.7, 0.8]

# Create a QuantumCircuit with 4 qubits
qc = QuantumCircuit(4)

# Apply the first layer of RY rotations
for i in range(4):
    qc.ry(angles_layer_1[i], i)

# Apply the first layer of CNOTs
qc.cx(0, 1)
qc.cx(1, 2)
qc.cx(2, 3)

# Apply the second layer of RY rotations
for i in range(4):
    qc.ry(angles_layer_2[i], i)

# Apply the second layer of CNOTs
qc.cx(0, 1)
qc.cx(1, 2)
qc.cx(2, 3)