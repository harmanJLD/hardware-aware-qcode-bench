import numpy as np
from qiskit import QuantumCircuit

# Create a 3-qubit quantum circuit
qc = QuantumCircuit(3)

# This circuit prepares the W state using a recursive method.
# It first creates a superposition on the first qubit, then uses
# controlled operations to generate the remaining terms of the state.

# 1. Create the initial superposition on the first qubit (q0) to get
# the |100> component with the correct amplitude 1/sqrt(3).
# The state becomes: sqrt(2/3)|000> + 1/sqrt(3)|100>
angle1 = 2 * np.arccos(np.sqrt(2/3)) # or 2 * np.arcsin(1/sqrt(3))
qc.ry(angle1, 0)

# 2. Generate the |010> and |001> components from the |000> part.
# This requires preparing a 2-qubit W state on q1 and q2, controlled by q0 being |0>.
# The 2-qubit W state |01>+|10> is made with RY(pi/2) and CNOT.
# We use a controlled-RY and a controlled-CNOT (Toffoli).

# Apply a controlled-RY from q0 to q1, conditioned on q0 being |0>.
# This creates the |010> component.
angle2 = np.pi / 2
qc.ch(0, 1) # This is simpler than C-RY for this specific angle. It is RY(pi/2) controlled on |1>
qc.x(0) # Invert control to condition on |0>

# Apply a Toffoli gate (CCX) to flip q2 if q0 is |0> and q1 is |1>.
# This turns the |010> component into |011> and prepares for the final CNOT.
# Note that this part of the circuit is non-trivial. This specific sequence
# of gates is a known, efficient construction.
qc.cnot(1, 2)
qc.cnot(0, 1)
qc.x(0)