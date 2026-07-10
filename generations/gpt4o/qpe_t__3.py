from qiskit import QuantumCircuit
from qiskit.circuit.library import QFT

# Initialize a Quantum Circuit with 4 qubits
qc = QuantumCircuit(4)

# Prepare the eigenstate |1> on qubit 3
qc.x(3)

# Apply Hadamard gates to the counting qubits (qubits 0, 1, 2)
qc.h([0, 1, 2])

# Apply controlled-T gates with appropriate powers
# Controlled-T = T
qc.cp(2 * 3.141592653589793 / 8, 0, 3)  # T^1
# Controlled-T^2
qc.cp(2 * 3.141592653589793 / 4, 1, 3)  # T^2
# Controlled-T^4
qc.cp(2 * 3.141592653589793 / 2, 2, 3)  # T^4

# Apply the inverse QFT on the counting qubits (qubits 0, 1, 2)
# The inverse QFT includes the required SWAP gates
qc.append(QFT(3, inverse=True, do_swaps=True), [0, 1, 2])

# The circuit 'qc' is now ready for further instructions or execution