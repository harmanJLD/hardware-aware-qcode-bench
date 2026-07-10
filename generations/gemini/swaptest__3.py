from qiskit import QuantumCircuit

# Initialize a 3-qubit quantum circuit
qc = QuantumCircuit(3)

# Prepare the states for the test
# Prepare qubit 1 in state |1>
qc.x(1)
# Prepare qubit 2 in state |+>
qc.h(2)

# Apply the SWAP test circuit structure
# Apply Hadamard to the ancilla (qubit 0)
qc.h(0)

# Apply the controlled-SWAP (Fredkin) gate
# a.k.a. cswap(control, target1, target2)
qc.cswap(0, 1, 2)

# Apply Hadamard to the ancilla again
qc.h(0)