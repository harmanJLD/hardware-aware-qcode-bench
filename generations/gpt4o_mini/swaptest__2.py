from qiskit import QuantumCircuit

# Create a QuantumCircuit with 3 qubits
qc = QuantumCircuit(3)

# Prepare qubit 1 in |1>
qc.x(1)

# Prepare qubit 2 in |+>
qc.h(2)

# Apply H to the ancilla (qubit 0)
qc.h(0)

# Apply controlled-SWAP on qubits 1 and 2 controlled by the ancilla (qubit 0)
qc.swap(1, 2).c_if(0, 1)  # Control SWAP operation

# Apply H to the ancilla (qubit 0)
qc.h(0)