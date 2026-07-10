from qiskit import QuantumCircuit

# Create a quantum circuit with 3 qubits
qc = QuantumCircuit(3)

# Prepare the initial states
qc.x(1)  # Prepare qubit 1 in |1>
qc.h(2)  # Prepare qubit 2 in |+> = H|0>

# Apply H to the ancilla qubit (qubit 0)
qc.h(0)

# Apply the controlled-SWAP gate, controlled by qubit 0 (ancilla)
qc.cswap(0, 1, 2)

# Apply H to the ancilla qubit again
qc.h(0)