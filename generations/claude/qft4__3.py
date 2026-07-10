from qiskit import QuantumCircuit
import numpy as np

qc = QuantumCircuit(4)

# QFT on 4 qubits (qubit 0 is LSB)
# Apply QFT starting from most significant qubit (qubit 3)

# Qubit 3
qc.h(3)
qc.cp(np.pi/2, 2, 3)
qc.cp(np.pi/4, 1, 3)
qc.cp(np.pi/8, 0, 3)

# Qubit 2
qc.h(2)
qc.cp(np.pi/2, 1, 2)
qc.cp(np.pi/4, 0, 2)

# Qubit 1
qc.h(1)
qc.cp(np.pi/2, 0, 1)

# Qubit 0
qc.h(0)

# Qubit reversal SWAP gates
qc.swap(0, 3)
qc.swap(1, 2)