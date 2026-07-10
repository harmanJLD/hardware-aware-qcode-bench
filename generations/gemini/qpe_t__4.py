import numpy as np
from qiskit.circuit import QuantumCircuit

# Initialize a QuantumCircuit with 3 counting qubits and 1 target qubit
# Qubits 0-2 are counting qubits (0 is LSB)
# Qubit 3 is the target qubit
qc = QuantumCircuit(4)

# 1. Prepare the eigenstate |1> on the target qubit (qubit 3).
# The T gate's eigenvalue for |1> is exp(i*pi/4).
qc.x(3)

# 2. Put the counting qubits in a superposition state.
qc.h(range(3))

# 3. Apply the controlled-unitary operations.
# The unitary is the T gate. We apply controlled-T^(2^j).
# Qubit 0 (LSB) controls T^1 = T = P(pi/4)
qc.cp(np.pi / 4, 0, 3)
# Qubit 1 controls T^2 = S = P(pi/2)
qc.cp(np.pi / 2, 1, 3)
# Qubit 2 (MSB) controls T^4 = Z = P(pi)
qc.cp(np.pi, 2, 3)

# 4. Apply the inverse Quantum Fourier Transform to the counting qubits.
# This is an explicit implementation for 3 qubits (0, 1, 2)
# where qubit 2 is the most significant bit.
qc.barrier()

# Gates for MSB (qubit 2)
qc.h(2)
qc.cp(-np.pi / 2, 1, 2)  # Controlled-Sdg gate
qc.cp(-np.pi / 4, 0, 2)  # Controlled-Tdg gate

# Gates for qubit 1
qc.h(1)
qc.cp(-np.pi / 2, 0, 1)  # Controlled-Sdg gate

# Gate for LSB (qubit 0)
qc.h(0)

# Final SWAPs to reverse the bit order of the counting register
qc.swap(0, 2)