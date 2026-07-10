from qiskit import QuantumCircuit
import math

qc = QuantumCircuit(4)

# QFT on 4 qubits (qubit 0 is LSB)
# Process qubits from most significant (qubit 3) to least significant (qubit 0)

# Qubit 3
qc.h(3)
qc.cp(math.pi/2, 2, 3)
qc.cp(math.pi/4, 1, 3)
qc.cp(math.pi/8, 0, 3)

# Qubit 2
qc.h(2)
qc.cp(math.pi/2, 1, 2)
qc.cp(math.pi/4, 0, 2)

# Qubit 1
qc.h(1)
qc.cp(math.pi/2, 0, 1)

# Qubit 0
qc.h(0)

# Qubit-reversal SWAP gates
qc.swap(0, 3)
qc.swap(1, 2)