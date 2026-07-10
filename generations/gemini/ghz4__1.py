from qiskit import QuantumCircuit

# Create a quantum circuit with 4 qubits
qc = QuantumCircuit(4)

# Apply a Hadamard gate to the first qubit to create superposition
qc.h(0)

# Apply a chain of CNOT gates to entangle the other qubits with the first one
qc.cx(0, 1)
qc.cx(0, 2)
qc.cx(0, 3)