from qiskit import QuantumCircuit

qc = QuantumCircuit(3)

# Prepare qubit 1 in |1>
qc.x(1)

# Prepare qubit 2 in |+> = H|0>
qc.h(2)

# Apply H to ancilla (qubit 0)
qc.h(0)

# Controlled-SWAP (Fredkin gate): swap qubits 1 and 2, controlled on qubit 0
qc.cswap(0, 1, 2)

# Apply H to ancilla (qubit 0)
qc.h(0)