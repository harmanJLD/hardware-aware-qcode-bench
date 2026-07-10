from qiskit import QuantumCircuit

# Create a QuantumCircuit with 4 qubits
qc = QuantumCircuit(4)

# Apply a Hadamard gate to the first qubit to create superposition
qc.h(0)

# Apply a series of CNOT gates to entangle the other qubits
qc.cx(0, 1)
qc.cx(0, 2)
qc.cx(0, 3)