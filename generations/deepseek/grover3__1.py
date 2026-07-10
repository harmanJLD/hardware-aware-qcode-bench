from qiskit import QuantumCircuit

# Create a Quantum Circuit with 3 qubits
qc = QuantumCircuit(3)

# Initial Hadamard gates
qc.h([0, 1, 2])

# Phase oracle for the marked state |101>
qc.cz(0, 2)  # Apply controlled-Z gate between qubit 0 and qubit 2

# Diffuser (inversion about the mean)
qc.h([0, 1, 2])
qc.x([0, 1, 2])
qc.h(2)
qc.ccx(0, 1, 2)
qc.h(2)
qc.x([0, 1, 2])
qc.h([0, 1, 2])