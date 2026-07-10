from qiskit import QuantumCircuit
from qiskit.circuit.library import QFT

# Create a quantum circuit with 4 qubits (3 counting qubits + 1 target)
qc = QuantumCircuit(4)

# Prepare the eigenstate |1> on qubit 3
qc.x(3)

# Apply Hadamard gates to all counting qubits
for qubit in range(3):
    qc.h(qubit)

# Apply controlled-T^(2^k) gates
for counting_qubit in range(3):
    power = 2 ** counting_qubit
    angle = 2 * 3.141592653589793 / (2 ** (4 - counting_qubit))  # T gate phase is pi/4
    for _ in range(power):
        qc.cp(angle, counting_qubit, 3)

# Apply inverse QFT on counting qubits (0-2)
qft = QFT(3, inverse=True, do_swaps=True)
qc.compose(qft, qubits=[0, 1, 2], inplace=True)