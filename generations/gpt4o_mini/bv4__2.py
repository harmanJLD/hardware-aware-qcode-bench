from qiskit import QuantumCircuit

# Define the quantum circuit with 4 qubits
qc = QuantumCircuit(4)

# Apply Hadamard gates to all qubits
qc.h([0, 1, 2, 3])

# Apply the phase oracle for the secret string s = 1101
qc.x(1)  # |1> for s_1
qc.x(0)  # |1> for s_0
qc.z(3)  # |1> for s_3
qc.z(2)  # |0> for s_2 (no action needed)

# Apply Hadamard gates to all qubits again
qc.h([0, 1, 2, 3])