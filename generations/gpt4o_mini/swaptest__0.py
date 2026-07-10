from qiskit import QuantumCircuit

qc = QuantumCircuit(3)

# Prepare |1> state on qubit 1
qc.x(1)

# Prepare |+> state on qubit 2
qc.h(2)

# Apply H to the ancilla (qubit 0)
qc.h(0)

# Apply controlled-SWAP gate between qubits 1 and 2 controlled by ancilla (qubit 0)
qc.swap(1, 2).c_if(0, 1)  # Controlled-SWAP operation

# Apply H on the ancilla (qubit 0) again
qc.h(0)