from qiskit import QuantumCircuit

# Create a QuantumCircuit with 3 qubits
qc = QuantumCircuit(3)

# Apply Hadamard gates to all qubits
qc.h([0, 1, 2])

# Define the phase oracle for f(x) = x_0 XOR x_1
# The phase oracle |x> -> (-1)^(f(x))|x> can be implemented using controlled-Z gates
qc.cz(0, 1)

# Apply Hadamard gates to all qubits again
qc.h([0, 1, 2])