from qiskit import QuantumCircuit

# Define a 4-qubit Quantum Circuit
qc = QuantumCircuit(4)

# Apply Hadamard gates to all qubits
qc.h(range(4))

# Implement the phase oracle for the secret string s = 1101
qc.cz(0, 3)  # Controlled Z gate between qubit 0 and 3
qc.cz(1, 3)  # Controlled Z gate between qubit 1 and 3
qc.cz(3, 3)  # Z gate on qubit 3

# Apply Hadamard gates to all qubits again
qc.h(range(4))