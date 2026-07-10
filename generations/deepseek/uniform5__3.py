from qiskit import QuantumCircuit

# Create a quantum circuit with 5 qubits
qc = QuantumCircuit(5)

# Apply Hadamard gates to all qubits to create superposition
for qubit in range(5):
    qc.h(qubit)