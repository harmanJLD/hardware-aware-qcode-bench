from qiskit import QuantumCircuit

qc = QuantumCircuit(3)

# Initial Hadamards
qc.h(0)
qc.h(1)
qc.h(2)

# Phase oracle for |101⟩ (qubit 0 = 1, qubit 1 = 0, qubit 2 = 1)
qc.x(1)  # Flip qubit 1 since we want it to be 0
qc.ccz(0, 1, 2)  # Multi-controlled Z gate
qc.x(1)  # Flip back

# Diffuser
qc.h(0)
qc.h(1)
qc.h(2)
qc.x(0)
qc.x(1)
qc.x(2)
qc.ccz(0, 1, 2)
qc.x(0)
qc.x(1)
qc.x(2)
qc.h(0)
qc.h(1)
qc.h(2)