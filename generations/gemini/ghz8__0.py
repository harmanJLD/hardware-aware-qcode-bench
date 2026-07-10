from qiskit import QuantumCircuit

# Define the number of qubits
num_qubits = 8

# Create a QuantumCircuit object
qc = QuantumCircuit(num_qubits)

# Apply a Hadamard gate to the first qubit to create superposition
qc.h(0)

# Apply a chain of CNOT gates to entangle the other qubits
for i in range(num_qubits - 1):
    qc.cx(i, i + 1)