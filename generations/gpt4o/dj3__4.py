from qiskit import QuantumCircuit

# Create a quantum circuit with 3 qubits
qc = QuantumCircuit(3)

# Apply Hadamard gates to all qubits
qc.h(range(3))

# Implement the phase oracle for f(x) = x_0 XOR x_1
qc.cx(0, 2)
qc.cx(1, 2)

# Apply Hadamard gates to all qubits again
qc.h(range(3))