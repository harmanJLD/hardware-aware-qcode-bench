from qiskit import QuantumCircuit

# Define the number of qubits
num_qubits = 4

# Create a QuantumCircuit object
qc = QuantumCircuit(num_qubits)

# Define the angles for the RY gates
layer1_angles = [0.1, 0.2, 0.3, 0.4]
layer2_angles = [0.5, 0.6, 0.7, 0.8]

# --- Layer 1 ---
# Apply RY gates to all qubits
for i in range(num_qubits):
    qc.ry(layer1_angles[i], i)

# Apply linear entanglement with CX gates
qc.cx(0, 1)
qc.cx(1, 2)
qc.cx(2, 3)

# --- Layer 2 ---
# Apply RY gates to all qubits
for i in range(num_qubits):
    qc.ry(layer2_angles[i], i)

# Apply linear entanglement with CX gates
qc.cx(0, 1)
qc.cx(1, 2)
qc.cx(2, 3)