from qiskit import QuantumCircuit

qc = QuantumCircuit(3)

# Apply Hadamard gate to the first qubit
qc.h(0)

# Apply CNOT gates to create the W state
qc.cx(0, 1)
qc.cx(0, 2)

# Apply a phase rotation to the second and third qubits
qc.z(1)
qc.z(2)