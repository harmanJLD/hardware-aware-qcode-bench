from qiskit import QuantumCircuit
import math

qc = QuantumCircuit(3)

# Prepare the W state: (|001> + |010> + |100>)/sqrt(3)
# Using a construction method with controlled operations

# Start with |000>
# Apply rotations to create the W state

# First, create a superposition on qubit 0 with amplitude sqrt(1/3) for |1>
theta1 = 2 * math.asin(math.sqrt(1/3))
qc.ry(theta1, 0)

# If qubit 0 is |0>, create equal superposition between qubits 1 and 2
# The amplitude for |0> on qubit 0 is sqrt(2/3)
# We need to distribute this equally between qubits 1 and 2
theta2 = 2 * math.asin(math.sqrt(1/2))
qc.x(0)
qc.cry(theta2, 0, 1)
qc.x(0)

# Use controlled-NOT to transfer amplitude from qubit 1 to qubit 2 when qubit 0 is |0>
qc.x(0)
qc.ccx(0, 1, 2)
qc.cx(0, 1)
qc.x(0)