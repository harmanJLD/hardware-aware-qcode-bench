import numpy as np
from qiskit import QuantumCircuit

# Create a 3-qubit quantum circuit
qc = QuantumCircuit(3)

# This circuit prepares the W state (|001> + |010> + |100>)/sqrt(3)
# The method is constructive, building the superposition step-by-step.

# 1. Create the state sqrt(2/3)|0> + 1/sqrt(3)|1> on qubit 0.
# The |1> component will evolve into the |100> part of the W state.
# The |0> component will be used to generate the other two terms.
# For Ry(theta), the resulting state is cos(theta/2)|0> + sin(theta/2)|1>.
# We want sin(theta/2) = 1/sqrt(3), so theta = 2 * arcsin(1/sqrt(3)).
theta = 2 * np.arcsin(1 / np.sqrt(3))
qc.ry(theta, 0)
# The state is now sqrt(2/3)|000> + 1/sqrt(3)|100>

# 2. Transform the |000> component into (|010> + |001>)/sqrt(3).
# This is done by applying a transformation to q1 and q2 that is
# controlled by q0 being in the |0> state.
# A |0>-controlled gate is implemented as X * C-GATE * X on the control qubit.
qc.x(0)

# The transformation U on (q1, q2) must map |00> to (|10> + |01>)/sqrt(2).
# This can be achieved by the sequence: Ry(pi/2, q1), CX(q1, q2), X(q1).
# We apply the controlled version of this sequence.

# Controlled-Ry(pi/2) on q1, controlled by q0
qc.cry(np.pi / 2, 0, 1)

# Controlled-CX(q1, q2), controlled by q0 (a Toffoli gate)
qc.ccx(0, 1, 2)

# Controlled-X(q1), controlled by q0
qc.cx(0, 1)

# Revert the control qubit to its original state
qc.x(0)