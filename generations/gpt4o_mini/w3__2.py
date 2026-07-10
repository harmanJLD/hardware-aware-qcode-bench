from qiskit import QuantumCircuit
import numpy as np

qc = QuantumCircuit(3)

# Apply Hadamard gate to the first qubit
qc.h(0)

# Apply CNOT gates to create superposition
qc.cx(0, 1)
qc.cx(0, 2)

# Normalize the state to prepare the W state
qc.initialize(np.array([0, 1/np.sqrt(3), 1/np.sqrt(3), 1/np.sqrt(3), 0, 0, 0, 0]), [0, 1, 2])