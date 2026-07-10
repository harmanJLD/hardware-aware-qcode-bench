import numpy as np
from qiskit.circuit import QuantumCircuit

# Create a 3-qubit quantum circuit
qc = QuantumCircuit(3)

# This method for preparing a W-state is generalizable.
# It progressively creates the superposition.

# Step 1: Create a superposition on the first qubit.
# The angle is chosen to set the probability of |1> to 1/3.
# P(|1>) = sin^2(theta/2) = 1/3  => theta = 2 * arcsin(1/sqrt(3))
angle = 2 * np.arcsin(1 / np.sqrt(3))
qc.ry(angle, 0)

# Step 2: If the first qubit is |0>, create a superposition on the second qubit.
# This is a controlled-Hadamard, but controlled on the |0> state.
qc.x(0)
qc.ch(0, 1)
qc.x(0)

# Step 3: If the first two qubits are |00>, flip the third qubit.
# This is a Toffoli gate (CCX), but controlled on the |00> state.
qc.x([0, 1])
qc.ccx(0, 1, 2)
qc.x([0, 1])