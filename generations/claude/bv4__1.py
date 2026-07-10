from qiskit import QuantumCircuit

qc = QuantumCircuit(4)

# Apply Hadamards to all qubits
qc.h(range(4))

# Apply phase oracle for secret string s = 1101 (s_0=1, s_1=1, s_2=0, s_3=1)
# Phase oracle applies (-1)^(s·x) = (-1)^(s_0*x_0 + s_1*x_1 + s_2*x_2 + s_3*x_3)
# Apply Z gate to qubit i if s_i = 1
qc.z(0)  # s_0 = 1
qc.z(1)  # s_1 = 1
# s_2 = 0, so no gate on qubit 2
qc.z(3)  # s_3 = 1

# Apply Hadamards to all qubits
qc.h(range(4))