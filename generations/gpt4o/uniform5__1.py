from qiskit import QuantumCircuit

# Create a Quantum Circuit with 5 qubits
qc = QuantumCircuit(5)

# Apply Hadamard gate to each qubit to create uniform superposition
qc.h(range(5))