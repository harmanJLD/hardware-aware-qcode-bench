import numpy as np
from qiskit import QuantumCircuit
from qiskit.circuit.library import QFT

# Create a Quantum Circuit with 3 counting qubits and 1 target qubit
# Qubits 0-2 are the counting register, qubit 3 is the target
qc = QuantumCircuit(4, name="QPE_T_gate")

# 1. Initialize the state
# Apply an X gate to the target qubit to prepare the eigenstate |1>
qc.x(3)

# Apply Hadamard gates to the counting qubits to create a superposition
qc.h([0, 1, 2])

# 2. Apply controlled-unitary operations (controlled powers of T)
# The T gate has a phase of e^(i*pi/4).
# We apply C-T^(2^k) for each counting qubit k.
# Qubit 0 (LSB) controls T^1 = T = P(pi/4)
qc.cp(np.pi / 4, 0, 3)
# Qubit 1 controls T^2 = S = P(pi/2)
qc.cp(np.pi / 2, 1, 3)
# Qubit 2 (MSB) controls T^4 = Z = P(pi)
qc.cp(np.pi, 2, 3)

# 3. Apply the inverse Quantum Fourier Transform on the counting register
# The QFT class with default settings includes the final SWAP gates and
# assumes qubit 0 is the least significant bit.
iqft_gate = QFT(num_qubits=3, inverse=True, name="IQFT")
qc.append(iqft_gate, [0, 1, 2])