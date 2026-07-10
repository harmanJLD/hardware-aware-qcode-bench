from qiskit import QuantumCircuit

# Define the QuantumCircuit
qc = QuantumCircuit(3)

# Prepare the initial states
qc.x(1)         # Prepare qubit 1 in |1⟩
qc.h(2)        # Prepare qubit 2 in |+⟩

# Apply H to the ancilla qubit (qubit 0)
qc.h(0)

# Apply controlled-SWAP (CSWAP) with the ancilla as control
qc.cswap(0, 1, 2)

# Apply H to the ancilla qubit (qubit 0) again
qc.h(0)