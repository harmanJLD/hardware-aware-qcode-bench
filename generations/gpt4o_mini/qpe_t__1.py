from qiskit import QuantumCircuit
from qiskit.circuit.library import QFT

# Create a QuantumCircuit with 4 qubits (3 counting qubits and 1 target qubit)
qc = QuantumCircuit(4)

# Prepare the target qubit in the |1> state
qc.x(3)

# Apply Hadamard gates to the counting qubits (0-2)
qc.h([0, 1, 2])

# Apply controlled T gates for phase estimation
qc.cp(0.125 * 3.14159, 0, 3)  # Controlled T gate (T^1)
qc.cp(0.25 * 3.14159, 1, 3)   # Controlled T^2 gate (T^2)
qc.cp(0.5 * 3.14159, 2, 3)    # Controlled T^4 gate (T^3)

# Apply the inverse QFT
qft = QFT(3, inverse=True)
qc.append(qft, [0, 1, 2])

# Include SWAP gates for the inverse QFT
qc.swap(0, 2)