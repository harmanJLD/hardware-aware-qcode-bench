from qiskit import QuantumCircuit
import numpy as np

# Create a 4-qubit quantum circuit
# Qubit 0 is the least significant qubit.
qc = QuantumCircuit(4)

# --- Apply the QFT core ---
# The standard QFT circuit applies H and controlled rotations
# starting from the most significant qubit.

# Operations on qubit 3 (MSB)
qc.h(3)
qc.cp(np.pi / 2, 2, 3)
qc.cp(np.pi / 4, 1, 3)
qc.cp(np.pi / 8, 0, 3)

# Operations on qubit 2
qc.h(2)
qc.cp(np.pi / 2, 1, 2)
qc.cp(np.pi / 4, 0, 2)

# Operations on qubit 1
qc.h(1)
qc.cp(np.pi / 2, 0, 1)

# Operation on qubit 0 (LSB)
qc.h(0)

# --- Apply the final SWAP gates to reverse the qubit order ---
# Swap qubit 0 with 3, and qubit 1 with 2.
qc.swap(0, 3)
qc.swap(1, 2)