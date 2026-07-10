from qiskit import QuantumCircuit

qc = QuantumCircuit(3)

# Prepare qubit 1 in |1>
qc.x(1)

# Prepare qubit 2 in |+>
qc.h(2)

# SWAP test
qc.h(0)  # Hadamard on ancilla
qc.cswap(0, 1, 2)  # Controlled-SWAP with control=0, targets=1,2
qc.h(0)  # Hadamard on ancilla