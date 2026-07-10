from qiskit import QuantumCircuit
import numpy as np

# Create a quantum circuit with 3 counting qubits and 1 target qubit
qc = QuantumCircuit(4)

# Prepare the target qubit (qubit 3) in the |1> eigenstate
qc.x(3)

# Apply Hadamard gates to the counting qubits (qubits 0-2)
for qubit in range(3):
    qc.h(qubit)

# Apply controlled-T^(2^k) gates
for counting_qubit in range(3):
    for _ in range(2 ** counting_qubit):
        # Controlled-T gate with control on 'counting_qubit' and target on qubit 3
        # T gate is a phase gate with angle pi/4
        qc.cp(np.pi/4, counting_qubit, 3)

# Apply inverse QFT (including SWAPs)
# First, swap qubits to reverse the order
qc.swap(0, 2)

# Then apply the inverse QFT without the final swaps
for qubit in range(3):
    # Apply Hadamard to the current qubit
    qc.h(qubit)
    # Apply controlled rotations with decreasing angle
    for next_qubit in range(qubit + 1, 3):
        angle = -np.pi / (2 ** (next_qubit - qubit))
        qc.cp(angle, next_qubit, qubit)