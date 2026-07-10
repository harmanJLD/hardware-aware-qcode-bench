from qiskit import QuantumCircuit
import numpy as np

qc = QuantumCircuit(3)

# Prepare the W state: (|001> + |010> + |100>)/sqrt(3)
# Using a decomposition approach

# Start with |000>
# Apply rotations to create the W state

# First, create a superposition on qubit 0
theta1 = 2 * np.arccos(np.sqrt(2/3))
qc.ry(theta1, 0)

# Controlled operation to distribute amplitude
qc.cx(0, 1)

# Apply rotation on qubit 1 when qubit 0 is |1>
theta2 = 2 * np.arctan(np.sqrt(2))
qc.x(0)
qc.cry(theta2, 0, 2)
qc.x(0)

# Swap to get correct distribution
qc.cx(0, 1)
qc.x(0)
qc.ccx(0, 1, 2)
qc.x(0)
qc.cx(0, 1)

# Adjust to get W state
qc.x(0)
qc.x(1)