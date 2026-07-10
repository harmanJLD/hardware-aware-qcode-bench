from qiskit import QuantumCircuit

# Initialize a 3-qubit quantum circuit
qc = QuantumCircuit(3)

# Apply Hadamard gates to all qubits to create superposition
qc.h(range(3))

# Apply the phase oracle for the balanced function f(x) = x_0 XOR x_1
# This oracle applies a phase of -1 to the states |01> and |10>
# on the first two qubits (q0, q1), leaving q2 unaffected.
qc.cx(0, 1)
qc.z(1)
qc.cx(0, 1)

# Apply Hadamard gates to the input qubits again
qc.h(range(3))