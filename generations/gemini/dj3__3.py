from qiskit import QuantumCircuit

# Initialize a 3-qubit quantum circuit
qc = QuantumCircuit(3)

# Step 1: Apply Hadamard gates to all qubits
qc.h([0, 1, 2])

# Insert a barrier for visual separation
qc.barrier()

# Step 2: Implement the phase oracle for f(x) = x_0 XOR x_1
# This oracle applies a phase of -1 if x_0 != x_1, and +1 otherwise.
# A common way to implement a phase oracle for XOR is using a CNOT-Z-CNOT
# sequence. This applies the phase (-1)^(x_0 XOR x_1) to the state |x_0 x_1>.
# Qubit 2 is unaffected by this oracle as f(x) does not depend on x_2.
qc.cx(0, 1)
qc.z(1)
qc.cx(0, 1)

# Insert a barrier for visual separation
qc.barrier()

# Step 3: Apply Hadamard gates to all qubits again
qc.h([0, 1, 2])