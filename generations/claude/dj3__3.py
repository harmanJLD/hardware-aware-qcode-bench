from qiskit import QuantumCircuit

qc = QuantumCircuit(3)

# Initial Hadamards on all qubits
qc.h(0)
qc.h(1)
qc.h(2)

# Phase oracle for f(x) = x_0 XOR x_1
# This function marks states where x_0 XOR x_1 = 1 with a phase flip
# x_0 XOR x_1 = 1 when exactly one of x_0 or x_1 is 1
# We can implement this using: CZ(0,1) sandwiched between X gates
qc.x(0)
qc.x(1)
qc.cz(0, 1)
qc.x(0)
qc.x(1)
qc.cz(0, 1)

# Final Hadamards on all qubits
qc.h(0)
qc.h(1)
qc.h(2)