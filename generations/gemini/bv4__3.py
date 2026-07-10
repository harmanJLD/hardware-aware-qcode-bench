from qiskit import QuantumCircuit

# Create a 4-qubit quantum circuit
qc = QuantumCircuit(4)

# 1. Apply Hadamard gates to all qubits to create superposition
qc.h(range(4))

# 2. Apply the phase oracle for the secret string s=(s_3,s_2,s_1,s_0)=(1,0,1,1)
# This is done by applying a Z gate to qubit i if s_i is 1.
# For s_0=1:
qc.z(0)
# For s_1=1:
qc.z(1)
# For s_2=0, we do nothing to qubit 2.
# For s_3=1:
qc.z(3)

# 3. Apply Hadamard gates to all qubits again
qc.h(range(4))