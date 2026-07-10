from qiskit import QuantumCircuit
import numpy as np

qc = QuantumCircuit(3)

# Apply H gate to the first qubit
qc.h(0)

# Apply CNOT gates to create the W state
qc.cx(0, 1)
qc.cx(0, 2)

# Apply a U3(θ, φ, λ) rotation to the first qubit to create the superposition
theta = np.arccos(1/np.sqrt(3))
qc.ry(2 * theta, 0)

# Apply a phase shift to the second and third qubits
qc.rz(np.pi/3, 1)
qc.rz(-np.pi/3, 2)