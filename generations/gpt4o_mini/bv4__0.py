from qiskit import QuantumCircuit

# Define the secret string
s = [1, 1, 0, 1]

# Create quantum circuit with 4 qubits
qc = QuantumCircuit(4)

# Apply Hadamard gates to all qubits
qc.h(range(4))

# Apply the phase oracle
for i in range(4):
    if s[i] == 1:
        qc.z(i)

# Apply Hadamard gates to all qubits again
qc.h(range(4))