from qiskit import QuantumCircuit

qc = QuantumCircuit(3)

# Initial Hadamard gates on all qubits
qc.h([0, 1, 2])

# Phase oracle for f(x) = x_0 XOR x_1
qc.cz(0, 1)

# Final Hadamard gates on all qubits
qc.h([0, 1, 2])