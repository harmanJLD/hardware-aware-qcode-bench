from qiskit import QuantumCircuit

# Create a QuantumCircuit with 3 qubits
qc = QuantumCircuit(3)

# Initial Hadamard gates
qc.h([0, 1, 2])

# Phase oracle for the marked state |101>
qc.cz(0, 2)  # Apply a control-Z gate from qubit 0 to qubit 2
qc.cz(1, 2)  # Apply a control-Z gate from qubit 1 to qubit 2

# Diffuser (inversion about the mean)
qc.h([0, 1, 2])
qc.x([0, 1, 2])
qc.h(2)  # Only apply H to the last qubit for the control
qc.cz(0, 2)
qc.cz(1, 2)
qc.h(2)
qc.x([0, 1, 2])
qc.h([0, 1, 2])