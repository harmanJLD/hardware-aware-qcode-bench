from qiskit import QuantumCircuit

# Create a quantum circuit with 5 qubits
qc = QuantumCircuit(5)

# Apply Hadamard gates to all qubits to create a uniform superposition
for i in range(5):
    qc.h(i)