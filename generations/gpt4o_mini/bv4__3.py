from qiskit import QuantumCircuit

# Define the number of qubits
n = 4

# Create a Quantum Circuit with 4 qubits
qc = QuantumCircuit(n)

# Apply Hadamard gate to all qubits
qc.h(range(n))

# Apply the phase oracle for the secret string s = 1101
# The Oracle applies a phase of (-1)^(s.x) to the state |x>
qc.z(0)  # Apply Z gate (phase flip) to qubit 0
qc.z(1)  # Apply Z gate (phase flip) to qubit 1
qc.i(2)  # No operation on qubit 2
qc.z(3)  # Apply Z gate (phase flip) to qubit 3

# Apply Hadamard gate to all qubits again
qc.h(range(n))