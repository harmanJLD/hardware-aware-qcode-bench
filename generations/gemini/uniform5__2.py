from qiskit import QuantumCircuit

# Create a quantum circuit with 5 qubits
qc = QuantumCircuit(5)

# Apply Hadamard gates to all qubits to create the uniform superposition
# The state will be 1/sqrt(32) * sum_{i=0 to 31} |i>
qc.h(range(5))