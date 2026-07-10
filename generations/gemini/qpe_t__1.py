import numpy as np
from qiskit import QuantumCircuit
from qiskit.circuit.library import QFT

# Initialize a QuantumCircuit with 3 counting qubits and 1 target qubit
qc = QuantumCircuit(4)

# Prepare the target qubit (qubit 3) in the |1> eigenstate of the T gate
qc.x(3)

# Apply Hadamard gates to the counting qubits (qubits 0, 1, 2)
qc.h(range(3))

# Apply controlled-U operations, where U is the T gate.
# The power of U is 2^k for the k-th counting qubit.
# Qubit 0 is the least significant bit.
# Controlled-T^(2^0) = Controlled-T
qc.cp(np.pi / 4, 0, 3)
# Controlled-T^(2^1) = Controlled-T^2 = Controlled-S
qc.cp(np.pi / 2, 1, 3)
# Controlled-T^(2^2) = Controlled-T^4 = Controlled-Z
qc.cp(np.pi, 2, 3)

# Create the inverse Quantum Fourier Transform gate for 3 qubits, including SWAPs
iqft = QFT(num_qubits=3, inverse=True, do_swaps=True, name="IQFT")

# Apply the inverse QFT to the counting register.
# The QFT gate implementation expects qubits ordered from most to least significant.
# Our circuit defined qubit 2 as MSB and qubit 0 as LSB, so we apply the gate
# to the qubits in the order [2, 1, 0].
qc.append(iqft, [2, 1, 0])