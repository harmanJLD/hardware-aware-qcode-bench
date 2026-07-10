from qiskit import QuantumCircuit

# Define the number of qubits
num_qubits = 4

# Create a Quantum Circuit object
qc = QuantumCircuit(num_qubits)

# 1. Apply Hadamard gates to all qubits
qc.h(range(num_qubits))

# 2. Apply the phase oracle for the secret string s
# s_0=1, s_1=1, s_2=0, s_3=1
# The phase oracle applies a Z gate to qubit i if s_i = 1.
# Qiskit's bit ordering is q_n-1, ..., q_1, q_0.
# So s_i corresponds to qubit i.
qc.z(0)  # For s_0 = 1
qc.z(1)  # For s_1 = 1
# No gate on qubit 2 for s_2 = 0
qc.z(3)  # For s_3 = 1

# 3. Apply Hadamard gates to all qubits again
qc.h(range(num_qubits))