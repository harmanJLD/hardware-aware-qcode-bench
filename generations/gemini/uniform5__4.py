from qiskit import QuantumCircuit

# Create a quantum circuit with 5 qubits
qc = QuantumCircuit(5)

# Apply a Hadamard gate to each qubit to create a uniform superposition
for i in range(5):
    qc.h(i)