import numpy as np
from qiskit import QuantumCircuit

# Define the number of qubits
n = 4

# Create a QuantumCircuit object
qc = QuantumCircuit(n)

# --- QFT Core ---
# Apply gates from the most significant qubit (n-1) down to the least (0).
for target_qubit in range(n - 1, -1, -1):
    # Apply a Hadamard gate
    qc.h(target_qubit)
    
    # Apply the controlled phase rotations
    for control_qubit in range(target_qubit - 1, -1, -1):
        # Calculate the angle for the C-Phase gate
        # The rotation is pi / 2^(k-j)
        angle = np.pi / (2**(target_qubit - control_qubit))
        qc.cp(angle, control_qubit, target_qubit)

# --- Final Swaps ---
# Swap the qubits to reverse the order to match the standard QFT output
for i in range(n // 2):
    qc.swap(i, n - 1 - i)