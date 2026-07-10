from qiskit import QuantumCircuit

# Create a quantum circuit with 4 qubits
qc = QuantumCircuit(4)

# Apply Hadamard gates to all qubits
qc.h([0, 1, 2, 3])

# Apply the phase oracle for secret string s=1101 (s_0=1, s_1=1, s_2=0, s_3=1)
# This corresponds to applying Z gates to qubits 0, 1, and 3
qc.z(0)
qc.z(1)
qc.z(3)

# Apply Hadamard gates to all qubits again
qc.h([0, 1, 2, 3])