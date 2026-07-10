from qiskit import QuantumCircuit

# Define a QuantumCircuit with 5 qubits
qc = QuantumCircuit(5)

# Apply Hadamard gate to each qubit to create a uniform superposition
qc.h(range(5))