import numpy as np
from qiskit import QuantumCircuit

# Define the number of qubits
num_qubits = 4

# Create a QuantumCircuit object named qc
qc = QuantumCircuit(num_qubits)

# Apply the QFT rotations
# Loop from the most significant qubit to the least significant
for target_qubit in range(num_qubits - 1, -1, -1):
    # Apply Hadamard gate
    qc.h(target_qubit)
    
    # Apply controlled-phase rotations
    divisor = 2
    for control_qubit in range(target_qubit - 1, -1, -1):
        angle = np.pi / divisor
        qc.cp(angle, control_qubit, target_qubit)
        divisor *= 2

# Apply the final SWAP gates to reverse the qubit order
for i in range(num_qubits // 2):
    qc.swap(i, num_qubits - 1 - i)