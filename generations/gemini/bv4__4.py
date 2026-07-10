from qiskit import QuantumCircuit

# The number of qubits
n = 4

# The secret string s = 1101, where s_i corresponds to qubit i
# s_0=1, s_1=1, s_2=0, s_3=1
secret_string = [1, 1, 0, 1]

# Create a QuantumCircuit object
qc = QuantumCircuit(n)

# 1. Apply Hadamard gates to all qubits
qc.h(range(n))

# 2. Apply the phase oracle for the secret string
# The oracle applies a Z gate to qubit i if s_i is 1.
for i in range(n):
    if secret_string[i] == 1:
        qc.z(i)

# 3. Apply Hadamard gates to all qubits again
qc.h(range(n))