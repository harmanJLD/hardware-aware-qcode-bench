from qiskit import QuantumCircuit

# Initialize a quantum circuit with 3 qubits
qc = QuantumCircuit(3)

# Prepare qubit 1 in state |1>
qc.x(1)

# Prepare qubit 2 in state |+> = H|0>
qc.h(2)

# Apply H on the ancilla qubit (qubit 0)
qc.h(0)

# Apply controlled-SWAP of qubits 1 and 2, controlled on qubit 0
qc.cswap(0, 1, 2)

# Apply H on the ancilla qubit (qubit 0) again
qc.h(0)