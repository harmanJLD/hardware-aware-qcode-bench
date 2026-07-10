from qiskit import QuantumCircuit

qc = QuantumCircuit(4)

# Apply Hadamards to all qubits
for i in range(4):
    qc.h(i)

# Apply phase oracle for secret string s = 1101 (s_0=1, s_1=1, s_2=0, s_3=1)
# The oracle applies (-1)^(s·x) = (-1)^(s_0*x_0 + s_1*x_1 + s_2*x_2 + s_3*x_3)
# This is implemented by applying Z gates to qubits where s_i = 1
qc.z(0)  # s_0 = 1
qc.z(1)  # s_1 = 1
# No gate for qubit 2 since s_2 = 0
qc.z(3)  # s_3 = 1

# Apply Hadamards to all qubits
for i in range(4):
    qc.h(i)