from qiskit import QuantumCircuit

# Create a QuantumCircuit with 3 qubits
qc = QuantumCircuit(3)

# Prepare qubit 1 in the |1> state
qc.x(1)

# Prepare qubit 2 in the |+> state
qc.h(2)

# Apply H to the ancilla qubit (qubit 0)
qc.h(0)

# Apply controlled-SWAP with ancilla as the control and qubits 1 and 2 as the targets
qc.cswap(0, 1, 2)

# Apply H to the ancilla qubit again
qc.h(0)