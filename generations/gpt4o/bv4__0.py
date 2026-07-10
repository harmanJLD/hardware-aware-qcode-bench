from qiskit import QuantumCircuit

# Create quantum circuit with 4 qubits
qc = QuantumCircuit(4)

# Apply Hadamard gates to all qubits
qc.h(range(4))

# Phase oracle for secret string s = 1101
qc.z(0)  # Apply Z gate for s_0 = 1
qc.z(1)  # Apply Z gate for s_1 = 1
qc.z(3)  # Apply Z gate for s_3 = 1
# Note: no Z gate for s_2 = 0

# Apply Hadamard gates to all qubits again
qc.h(range(4))