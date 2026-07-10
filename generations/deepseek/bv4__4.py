from qiskit import QuantumCircuit

# Define the QuantumCircuit object with 4 qubits
qc = QuantumCircuit(4)

# Apply Hadamard gates to all qubits
qc.h([0, 1, 2, 3])

# Apply the phase oracle for the secret string s = [1, 1, 0, 1]
qc.cz(0, 3)
qc.cz(1, 3)
qc.cz(3, 3)  # This Z gate on qubit 3 is redundant since Z^2 = I, but included for completeness

# Apply Hadamard gates to all qubits again
qc.h([0, 1, 2, 3])