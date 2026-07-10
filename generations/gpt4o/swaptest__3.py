from qiskit import QuantumCircuit

# Create a QuantumCircuit with 3 qubits
qc = QuantumCircuit(3)

# Prepare qubit 1 in |1>
qc.x(1)

# Prepare qubit 2 in |+> = H|0>
qc.h(2)

# Apply H to the ancilla qubit (qubit 0)
qc.h(0)

# Apply controlled-SWAP on qubits 1 and 2, controlled by the ancilla qubit (qubit 0)
qc.cswap(0, 1, 2)

# Apply H to the ancilla qubit (qubit 0)
qc.h(0)