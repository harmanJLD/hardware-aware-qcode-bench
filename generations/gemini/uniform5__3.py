from qiskit import QuantumCircuit

# Create a quantum circuit with 5 qubits
qc = QuantumCircuit(5)

# Apply a Hadamard gate to each qubit to create the uniform superposition
qc.h(range(5))