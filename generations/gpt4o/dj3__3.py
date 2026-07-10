from qiskit import QuantumCircuit

# Create a QuantumCircuit with 3 qubits
qc = QuantumCircuit(3)

# Apply Hadamard gates on all qubits
qc.h([0, 1, 2])

# Implement the phase oracle for the balanced function f(x) = x_0 XOR x_1
qc.cx(0, 2)
qc.cx(1, 2)

# Apply Hadamard gates on all qubits
qc.h([0, 1, 2])