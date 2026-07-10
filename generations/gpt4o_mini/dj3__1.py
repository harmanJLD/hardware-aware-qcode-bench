from qiskit import QuantumCircuit

# Define the QuantumCircuit
qc = QuantumCircuit(3)

# Apply Hadamard gates to all qubits
qc.h([0, 1, 2])

# Phase oracle for balanced function f(x) = x_0 XOR x_1
qc.cx(0, 2)  # CNOT with control qubit 0 and target qubit 2
qc.cx(1, 2)  # CNOT with control qubit 1 and target qubit 2

# Apply Hadamard gates to all qubits again
qc.h([0, 1, 2])