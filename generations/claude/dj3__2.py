from qiskit import QuantumCircuit

qc = QuantumCircuit(3)

# Apply Hadamards on all qubits
qc.h(0)
qc.h(1)
qc.h(2)

# Phase oracle for f(x) = x_0 XOR x_1
# This applies a phase of -1 when x_0 XOR x_1 = 1
# Using CZ gate between qubits 0 and 1
qc.cz(0, 1)

# Apply Hadamards on all qubits
qc.h(0)
qc.h(1)
qc.h(2)