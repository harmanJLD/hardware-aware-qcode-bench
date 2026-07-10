import numpy as np
from qiskit import QuantumCircuit

# Define the number of qubits
n = 4

# Create a QuantumCircuit object
qc = QuantumCircuit(n)

# Apply the QFT core circuit
# For each qubit, apply a Hadamard gate, followed by controlled-phase rotations
for target_qubit in range(n):
    # Apply Hadamard to the target qubit
    qc.h(target_qubit)
    
    # Apply controlled-phase rotations with subsequent qubits as controls
    for control_qubit in range(target_qubit + 1, n):
        # Calculate the angle for the controlled-phase gate
        # The angle is pi / 2^(k), where k is the distance between the qubits
        angle = np.pi / (2**(control_qubit - target_qubit))
        qc.cp(angle, control_qubit, target_qubit)

# Add the final SWAP gates to reverse the order of the qubits
# This is necessary because the QFT algorithm naturally produces the output
# in bit-reversed order.
for i in range(n // 2):
    qc.swap(i, n - 1 - i)