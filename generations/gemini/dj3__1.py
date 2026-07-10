from qiskit import QuantumCircuit

# Create a quantum circuit with 3 qubits
qc = QuantumCircuit(3)

# 1. Apply Hadamards to all qubits
qc.h(range(3))

# 2. Apply the phase oracle for f(x) = x_0 XOR x_1
# This corresponds to applying a Z gate to qubit 0 and qubit 1.
# The phase is (-1)^(x_0 + x_1) which is equivalent to (-1)^(x_0 XOR x_1).
qc.z(0)
qc.z(1)

# 3. Apply Hadamards to all qubits again
qc.h(range(3))