from qiskit import QuantumCircuit
import numpy as np

qc = QuantumCircuit(3)

# Prepare the W state: (|001> + |010> + |100>)/sqrt(3)
# Using a construction method for W states

# Start with |001>
qc.x(2)

# Apply controlled rotations to create equal superposition
# Angle for first rotation: theta1 such that sin(theta1) = sqrt(1/3)
theta1 = 2 * np.arcsin(np.sqrt(1/3))
qc.ry(theta1, 1)
qc.ch(1, 2)

# Angle for second rotation: theta2 such that sin(theta2) = sqrt(1/2)
theta2 = 2 * np.arcsin(np.sqrt(1/2))
qc.x(1)
qc.cry(theta2, 1, 0)
qc.x(1)

# Correct the phases
qc.cx(0, 2)
qc.cx(1, 2)