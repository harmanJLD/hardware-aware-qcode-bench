from qiskit import QuantumCircuit

# Create a quantum circuit with 3 qubits
qc = QuantumCircuit(3)

# Prepare the states for the test
# Qubit 1 in state |1>
qc.x(1)
# Qubit 2 in state |+>
qc.h(2)

# --- Start of the SWAP test ---
# Apply Hadamard gate to the ancilla qubit (qubit 0)
qc.h(0)

# Apply the controlled-SWAP (Fredkin) gate
# Control qubit is 0, target qubits are 1 and 2
qc.cswap(0, 1, 2)

# Apply Hadamard gate to the ancilla qubit again
qc.h(0)
# --- End of the SWAP test ---