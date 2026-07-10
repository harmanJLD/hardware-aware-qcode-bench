from qiskit import QuantumCircuit
from qiskit.circuit.library import QFT

# Create a quantum circuit with 4 qubits
qc = QuantumCircuit(4)

# Prepare the state |1> on the eigenstate qubit (qubit 3)
qc.x(3)

# Apply Hadamard gates to the counting qubits (qubits 0-2)
qc.h(0)
qc.h(1)
qc.h(2)

# Apply controlled-T gates for phase estimation
# Controlled T^2 gate (controlled S gate) to qubit 3 with control from qubit 1
qc.cp(2 * 3.141592653589793 / 4, 1, 3)  # T^2 = S

# Controlled T^1 gate to qubit 3 with control from qubit 0
qc.cp(3.141592653589793 / 4, 0, 3)  # T

# Controlled T^4 gate (controlled Z gate) to qubit 3 with control from qubit 2
qc.cp(4 * 3.141592653589793 / 4, 2, 3)  # T^4 = Z

# Apply the inverse QFT to the counting qubits (qubits 0-2)
qc.append(QFT(3, inverse=True, do_swaps=True), [0, 1, 2])

# The circuit is now ready for use but without measurement