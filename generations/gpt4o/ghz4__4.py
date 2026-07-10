from qiskit import QuantumCircuit

# Create a 4-qubit quantum circuit
qc = QuantumCircuit(4)

# Apply a Hadamard gate on the first qubit
qc.h(0)

# Apply CNOT gates to create entanglement
qc.cx(0, 1)
qc.cx(1, 2)
qc.cx(2, 3)