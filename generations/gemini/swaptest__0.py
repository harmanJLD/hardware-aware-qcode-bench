from qiskit.circuit import QuantumCircuit

# Create a QuantumCircuit object with 3 qubits
qc = QuantumCircuit(3)

# Prepare the states for the test
# Qubit 1 is prepared in |1>
qc.x(1)
# Qubit 2 is prepared in |+>
qc.h(2)

# Apply the SWAP test circuit
# 1. Apply Hadamard gate to the ancilla (qubit 0)
qc.h(0)

# 2. Apply controlled-SWAP gate
#    Ancilla (qubit 0) is the control
#    Qubits 1 and 2 are the targets
qc.cswap(0, 1, 2)

# 3. Apply Hadamard gate to the ancilla again
qc.h(0)