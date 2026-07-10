from qiskit import QuantumCircuit

# Initialize a 3-qubit quantum circuit
qc = QuantumCircuit(3)

# Prepare the states for qubits 1 and 2
# Qubit 1 in state |1>
qc.x(1)
# Qubit 2 in state |+>
qc.h(2)

# Apply the SWAP test circuit
# Apply H to the ancilla (qubit 0)
qc.h(0)
# Apply the controlled-SWAP (Fredkin gate)
qc.cswap(0, 1, 2)
# Apply H to the ancilla again
qc.h(0)