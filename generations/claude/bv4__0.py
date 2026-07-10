from qiskit import QuantumCircuit

qc = QuantumCircuit(4)

# Apply Hadamards to all qubits
qc.h([0, 1, 2, 3])

# Apply phase oracle for secret string s = "1101" (s_0=1, s_1=1, s_2=0, s_3=1)
# The phase oracle applies a Z gate to qubit i if s_i = 1
qc.z(0)
qc.z(1)
qc.z(3)

# Apply Hadamards to all qubits
qc.h([0, 1, 2, 3])