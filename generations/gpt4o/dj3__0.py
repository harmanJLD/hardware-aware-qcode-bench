from qiskit import QuantumCircuit

# Create a QuantumCircuit with 3 qubits
qc = QuantumCircuit(3)

# Apply Hadamard gates to all qubits
qc.h([0, 1, 2])

# Phase oracle for f(x) = x_0 XOR x_1
qc.cz(0, 1)
qc.cz(0, 2)
qc.cz(1, 2)

# Apply Hadamard gates to all qubits
qc.h([0, 1, 2])