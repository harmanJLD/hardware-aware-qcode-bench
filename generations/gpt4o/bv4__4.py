from qiskit import QuantumCircuit

# Initialize a quantum circuit with 4 qubits
qc = QuantumCircuit(4)

# Apply Hadamard gates to all qubits
qc.h(range(4))

# Apply the phase oracle for the secret string s = 1101
qc.cz(0, 3)  # Apply CZ gate between qubit 0 and qubit 3
qc.cz(1, 3)  # Apply CZ gate between qubit 1 and qubit 3
qc.z(3)      # Apply Z gate to qubit 3

# Apply Hadamard gates to all qubits again
qc.h(range(4))