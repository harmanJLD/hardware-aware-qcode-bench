from qiskit import QuantumCircuit

qc = QuantumCircuit(3)

# Initial Hadamards on all qubits
qc.h(0)
qc.h(1)
qc.h(2)

# Phase oracle for f(x) = x_0 XOR x_1
# This applies a phase of -1 when x_0 XOR x_1 = 1
# x_0 XOR x_1 = 1 when exactly one of x_0 or x_1 is 1
qc.cx(0, 2)
qc.cx(1, 2)
qc.cz(2, 0)
qc.cx(1, 2)
qc.cx(0, 2)

# Final Hadamards on all qubits
qc.h(0)
qc.h(1)
qc.h(2)