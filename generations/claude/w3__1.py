from qiskit import QuantumCircuit
import numpy as np

qc = QuantumCircuit(3)

# Prepare the W state: (|001> + |010> + |100>)/sqrt(3)
# Using a decomposition approach

# Start with |000>
# Apply gates to create the W state

# Step 1: Create superposition on first qubit with specific amplitude
theta1 = 2 * np.arccos(np.sqrt(2/3))
qc.ry(theta1, 0)

# Step 2: Controlled rotation on second qubit
theta2 = 2 * np.arccos(np.sqrt(1/2))
qc.x(0)
qc.cry(theta2, 0, 1)
qc.x(0)

# Step 3: Transfer amplitude to third qubit using controlled operations
qc.cx(1, 2)
qc.cx(0, 2)
qc.x(0)
qc.ccx(0, 1, 2)
qc.x(0)