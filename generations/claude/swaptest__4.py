from qiskit import QuantumCircuit

qc = QuantumCircuit(3)

# Prepare qubit 1 in |1>
qc.x(1)

# Prepare qubit 2 in |+>
qc.h(2)

# SWAP test circuit
# Apply H to ancilla (qubit 0)
qc.h(0)

# Controlled-SWAP (Fredkin gate) with control on qubit 0, swapping qubits 1 and 2
qc.cswap(0, 1, 2)

# Apply H to ancilla (qubit 0)
qc.h(0)