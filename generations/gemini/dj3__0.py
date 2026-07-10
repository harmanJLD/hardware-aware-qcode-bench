from qiskit.circuit import QuantumCircuit

# Initialize a 3-qubit quantum circuit
qc = QuantumCircuit(3)

# Step 1: Apply Hadamard gates to all qubits to create superposition
qc.h(range(3))

# Step 2: Apply the phase oracle for f(x) = x_0 XOR x_1.
# This oracle applies a phase of -1 if f(x)=1.
# For f(x) = x_0 XOR x_1, the corresponding operator is Z on qubit 0
# and Z on qubit 1, since (-1)^(x_0 XOR x_1) = (-1)^x_0 * (-1)^x_1.
qc.z(0)
qc.z(1)

# Step 3: Apply Hadamard gates to the first n qubits again
qc.h(range(3))