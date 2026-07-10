from qiskit import QuantumCircuit

# Define the QuantumCircuit object
qc = QuantumCircuit(3)

# Apply Hadamard gates to all qubits
qc.h([0, 1, 2])

# Implement the phase oracle for the balanced function f(x) = x_0 XOR x_1
qc.cx(0, 2)  # CNOT gate from qubit 0 to qubit 2
qc.cx(1, 2)  # CNOT gate from qubit 1 to qubit 2

# Apply Hadamard gates to all qubits again
qc.h([0, 1, 2])