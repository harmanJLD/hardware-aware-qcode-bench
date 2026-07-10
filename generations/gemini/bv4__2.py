from qiskit import QuantumCircuit

# Define the number of qubits
n = 4

# Create a QuantumCircuit object named qc
qc = QuantumCircuit(n)

# 1. Apply Hadamards to all qubits to create superposition
qc.h(range(n))

# 2. Apply the phase oracle for the secret string.
# The prompt specifies s_0=1, s_1=1, s_2=0, s_3=1.
# A phase of (-1) is applied if s_i=1. This corresponds
# to applying a Z gate on qubit i for each s_i=1.
# For s_0=1: apply Z on qubit 0
# For s_1=1: apply Z on qubit 1
# For s_2=0: do nothing (apply Identity)
# For s_3=1: apply Z on qubit 3
qc.z(0)
qc.z(1)
qc.z(3)

# 3. Apply Hadamards to all qubits again
qc.h(range(n))