from qiskit import QuantumCircuit
import math

qc = QuantumCircuit(4)

# Prepare eigenstate |1> on qubit 3
qc.x(3)

# Initialize counting qubits in superposition
qc.h(0)
qc.h(1)
qc.h(2)

# Controlled-U^(2^k) operations
# T gate has phase pi/4, so T = e^(i*pi/4) * P(pi/4) up to global phase
# We use controlled-P gates with appropriate angles

# Controlled-T^1 from qubit 0 (2^0 = 1)
qc.cp(math.pi/4, 0, 3)

# Controlled-T^2 from qubit 1 (2^1 = 2)
qc.cp(2 * math.pi/4, 1, 3)

# Controlled-T^4 from qubit 2 (2^2 = 4)
qc.cp(4 * math.pi/4, 2, 3)

# Inverse QFT on counting qubits (0, 1, 2)
# Swap first
qc.swap(0, 2)

# Inverse QFT
qc.h(2)
qc.cp(-math.pi/2, 1, 2)
qc.h(1)
qc.cp(-math.pi/4, 0, 2)
qc.cp(-math.pi/2, 0, 1)
qc.h(0)