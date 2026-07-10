from qiskit import QuantumCircuit

# Create a 4-qubit quantum circuit
qc = QuantumCircuit(4)

# Apply a Hadamard gate to the first qubit to create superposition
qc.h(0)

# Apply CNOT gates to entangle the first qubit with the others
qc.cx(0, 1)
qc.cx(0, 2)
qc.cx(0, 3)