from qiskit import QuantumCircuit

qc = QuantumCircuit(3)

# Prepare qubit 1 in |1>
qc.x(1)

# Prepare qubit 2 in |+>
qc.h(2)

# Apply H to the ancilla (qubit 0)
qc.h(0)

# Apply controlled-SWAP (CSWAP) controlled by the ancilla (qubit 0)
qc.cswap(0, 1, 2)

# Apply H to the ancilla (qubit 0) again
qc.h(0)