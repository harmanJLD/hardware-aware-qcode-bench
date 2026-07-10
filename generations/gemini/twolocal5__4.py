from qiskit.circuit import QuantumCircuit

# Define the number of qubits and the rotation angles
num_qubits = 5
ry_angles_1 = [0.1, 0.2, 0.3, 0.4, 0.5]
ry_angles_2 = [0.6, 0.7, 0.8, 0.9, 1.0]

# Create a QuantumCircuit object
qc = QuantumCircuit(num_qubits)

# --- First layer of the two-local ansatz ---
# Apply the first RY rotation layer
for i in range(num_qubits):
    qc.ry(ry_angles_1[i], i)

# Apply the circular CX entanglement layer
for i in range(num_qubits - 1):
    qc.cx(i, i + 1)
qc.cx(num_qubits - 1, 0)

# --- Second layer of the two-local ansatz ---
# Apply the second RY rotation layer
for i in range(num_qubits):
    qc.ry(ry_angles_2[i], i)