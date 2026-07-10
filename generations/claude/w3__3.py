from qiskit import QuantumCircuit
import numpy as np

qc = QuantumCircuit(3)

# Prepare the W state: (|001> + |010> + |100>)/sqrt(3)
# Using a decomposition approach

# Start with |000>
# First, create superposition on qubit 0
theta1 = 2 * np.arccos(np.sqrt(2/3))
qc.ry(theta1, 0)

# Controlled operation to distribute amplitude
qc.cx(0, 1)

# Create the right superposition on qubits 1 and 2
theta2 = 2 * np.arcsin(1/np.sqrt(2))
qc.x(0)
qc.cry(theta2, 0, 2)
qc.x(0)

# Swap to get the correct distribution
qc.cx(1, 2)
qc.cx(0, 1)
qc.cx(1, 2)