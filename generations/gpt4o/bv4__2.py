from qiskit import QuantumCircuit

# Define the number of qubits
n = 4

# Create a quantum circuit with 4 qubits
qc = QuantumCircuit(n)

# Apply Hadamard gates to all qubits
qc.h(range(n))

# Apply the phase oracle for the secret string s = 1101
qc.cz(0, 1)  # Apply CZ between qubits 0 and 1 for s_0 = 1
qc.cz(1, 2)  # Apply CZ between qubits 1 and 2 for s_1 = 1
# No CZ for s_2 = 0
qc.cz(3, 0)  # Apply CZ between qubits 3 and 0 for s_3 = 1

# Apply Hadamard gates to all qubits again
qc.h(range(n))