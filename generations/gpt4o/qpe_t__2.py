from qiskit import QuantumCircuit
from qiskit.circuit.library import QFT

# Create a quantum circuit with 4 qubits: 3 counting qubits and 1 target qubit
qc = QuantumCircuit(4)

# Prepare the target qubit in the eigenstate |1>
qc.x(3)

# Apply the controlled powers of the T gate
qc.cp(2 * 3.141592653589793 / 8, 2, 3)  # Controlled T^1 gate
qc.cp(2 * 3.141592653589793 / 4, 1, 3)  # Controlled T^2 gate
qc.cp(2 * 3.141592653589793 / 2, 0, 3)  # Controlled T^4 gate

# Apply the inverse QFT on the counting register
qc.append(QFT(3, inverse=True, do_swaps=True), range(3))