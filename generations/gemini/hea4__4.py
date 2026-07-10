from qiskit import QuantumCircuit

# Define the number of qubits and the rotation angles for each layer
num_qubits = 4
angles_layer1 = [0.1, 0.2, 0.3, 0.4]
angles_layer2 = [0.5, 0.6, 0.7, 0.8]

# Create a QuantumCircuit
qc = QuantumCircuit(num_qubits)

# --- Layer 1 ---
# Apply single-qubit RY rotations
for i in range(num_qubits):
    qc.ry(angles_layer1[i], i)

# Apply the entangling CX gates
qc.cx(0, 1)
qc.cx(1, 2)
qc.cx(2, 3)

# --- Layer 2 ---
# Apply single-qubit RY rotations
for i in range(num_qubits):
    qc.ry(angles_layer2[i], i)

# Apply the entangling CX gates
qc.cx(0, 1)
qc.cx(1, 2)
qc.cx(2, 3)