import numpy as np
from qiskit import QuantumCircuit

# Create a 3-qubit quantum circuit
qc = QuantumCircuit(3)

# This circuit prepares the W state using a standard construction method.
# The method first creates a superposition on the first qubit to set the
# amplitude of the |100> state, then uses a controlled operation to create
# a superposition of |001> and |010> conditional on the first qubit being |0>.

# 1. Apply a Y-rotation to the first qubit.
# The angle is chosen such that the amplitude of |1> is 1/sqrt(3).
# cos(theta/2)|0> + sin(theta/2)|1>
# We want sin(theta/2) = 1/sqrt(3), so theta = 2 * arcsin(1/sqrt(3)).
# The state becomes: sqrt(2/3)|000> + 1/sqrt(3)|100>
angle = 2 * np.arcsin(1 / np.sqrt(3))
qc.ry(angle, 0)

# 2. Apply a sub-circuit that transforms |000> into (|010> + |001>)/sqrt(2)
# and leaves |100> unchanged. This is done by controlling the sub-circuit
# on qubit 0 being in the |0> state.

# To control on |0>, we surround the controlled gates with X gates on the control qubit.
qc.x(0)

# The sub-circuit to transform |..00> to (|..10> + |..01>)/sqrt(2) is H(q1) CNOT(q1,q2) X(q1).
# We make each of these gates controlled by qubit 0.
qc.ch(0, 1)        # Controlled-Hadamard from q0 to q1
qc.ccx(0, 1, 2)      # Controlled-CNOT (Toffoli) from q0 and q1 to q2
qc.cnot(0, 1)        # Controlled-X from q0 to q1

# Uncompute the X gate on the control qubit.
qc.x(0)