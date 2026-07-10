from qiskit import QuantumCircuit

# Create a quantum circuit with 3 qubits
qc = QuantumCircuit(3)

# Apply Hadamard gates to all qubits
qc.h([0, 1, 2])

# Implement the phase oracle for f(x) = x_0 XOR x_1
# This is equivalent to a controlled-Z gate between qubits 0 and 1
qc.cz(0, 1)

# Apply Hadamard gates to all qubits again
qc.h([0, 1, 2])