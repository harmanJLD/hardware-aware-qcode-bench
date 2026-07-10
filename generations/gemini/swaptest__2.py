from qiskit.circuit import QuantumCircuit

# Create a QuantumCircuit with 3 qubits
qc = QuantumCircuit(3)

# Prepare the states for the test
# Prepare qubit 1 in the |1> state
qc.x(1)
# Prepare qubit 2 in the |+> state
qc.h(2)

# Apply the SWAP test circuit
# Apply H to the ancilla (qubit 0)
qc.h(0)
# Apply the controlled-SWAP gate (Fredkin gate)
# Control: qubit 0, Targets: qubits 1 and 2
qc.cswap(0, 1, 2)
# Apply H to the ancilla (qubit 0)
qc.h(0)