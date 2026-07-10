from qiskit.circuit import QuantumCircuit

# Define the number of qubits and layers
num_qubits = 4
num_layers = 2

# Define the angles for the RY gates
angles = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]

# Create a QuantumCircuit object
qc = QuantumCircuit(num_qubits)

# Build the hardware-efficient ansatz
for layer in range(num_layers):
    # Apply single-qubit rotations (RY)
    for qubit in range(num_qubits):
        angle_index = layer * num_qubits + qubit
        qc.ry(angles[angle_index], qubit)

    # Apply two-qubit entangling gates (CX)
    for qubit in range(num_qubits - 1):
        qc.cx(qubit, qubit + 1)