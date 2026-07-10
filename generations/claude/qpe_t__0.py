from qiskit import QuantumCircuit
import math

qc = QuantumCircuit(4)

# Prepare eigenstate |1> on qubit 3
qc.x(3)

# Prepare counting qubits in superposition
qc.h(0)
qc.h(1)
qc.h(2)

# Controlled powers of T gate
# T gate has phase pi/4, so T^k has phase k*pi/4
# Qubit 0 (least significant): controls T^(2^0) = T^1
qc.cp(math.pi/4, 0, 3)

# Qubit 1: controls T^(2^1) = T^2 = S
qc.cp(math.pi/2, 1, 3)

# Qubit 2 (most significant): controls T^(2^2) = T^4 = Z
qc.cp(math.pi, 2, 3)

# Inverse QFT on counting qubits (0, 1, 2)
# First SWAP qubits 0 and 2
qc.swap(0, 2)

# Inverse QFT operations
qc.h(2)
qc.cp(-math.pi/2, 1, 2)
qc.cp(-math.pi/4, 0, 2)
qc.h(1)
qc.cp(-math.pi/2, 0, 1)
qc.h(0)