from qiskit import QuantumCircuit

# The secret string is s = 1101 (s_0=1, s_1=1, s_2=0, s_3=1)
# The number of qubits is 4.

# 1. Initialize a quantum circuit
qc = QuantumCircuit(4)

# 2. Apply Hadamard gates to all qubits
qc.h(range(4))

# 3. Apply the phase oracle for s = 1101
# The oracle applies a Z gate to qubit i if s_i is 1.
# s_0 = 1
qc.z(0)
# s_1 = 1
qc.z(1)
# s_2 = 0 (do nothing)
# s_3 = 1
qc.z(3)

# 4. Apply Hadamard gates to all qubits again
qc.h(range(4))