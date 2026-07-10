import numpy as np
from qiskit.circuit import QuantumCircuit

# Define the number of qubits
n = 4

# Create a QuantumCircuit object
qc = QuantumCircuit(n)

# Apply the QFT rotations
# Loop through qubits from most significant to least significant
for i in range(n - 1, -1, -1):
    # Apply Hadamard gate
    qc.h(i)
    # Apply controlled-phase gates
    for j in range(i - 1, -1, -1):
        # Calculate the angle for the controlled-phase gate
        angle = np.pi / (2**(i - j))
        qc.cp(angle, i, j)

# Apply the final SWAP gates to reverse the qubit order
for i in range(n // 2):
    qc.swap(i, n - 1 - i)