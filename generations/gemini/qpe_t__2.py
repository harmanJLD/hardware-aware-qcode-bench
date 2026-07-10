import numpy as np
from qiskit import QuantumCircuit
from qiskit.circuit.library import QFT

# Define the number of counting and target qubits
n_counting = 3
target_qubit = 3

# Create the QuantumCircuit
# Qubits 0, 1, 2 are counting qubits
# Qubit 3 is the target qubit
qc = QuantumCircuit(n_counting + 1)

# --- 1. State Preparation ---

# Prepare the target qubit (qubit 3) in the |1> eigenstate of the T gate
qc.x(target_qubit)

# Apply Hadamard gates to the counting qubits (qubits 0, 1, 2)
for qubit in range(n_counting):
    qc.h(qubit)

# --- 2. Controlled Unitary Operations ---

# Apply controlled powers of the T gate.
# The phase of the T gate is pi/4.
# For each counting qubit k, we apply a controlled-U^(2^k) operation,
# where U = T. This is equivalent to a controlled-phase gate with an
# angle of (pi/4) * 2^k.
for k in range(n_counting):
    # Control qubit is k, target is the target_qubit
    # The phase is scaled by 2^k
    phase = (np.pi / 4) * (2**k)
    qc.cp(phase, k, target_qubit)

# --- 3. Inverse Quantum Fourier Transform ---

# Create the inverse QFT gate for the 3 counting qubits.
# The `do_swaps=True` argument (default) ensures the textbook QFT
# implementation, including the final SWAP gates to reverse qubit order.
iqft = QFT(num_qubits=n_counting, inverse=True, name='IQFT')

# Append the iQFT to the counting qubits (0, 1, 2)
# Qiskit's QFT acts on qubits from most to least significant.
# By convention, qubit 2 is MSB and qubit 0 is LSB.
qc.append(iqft, range(n_counting))