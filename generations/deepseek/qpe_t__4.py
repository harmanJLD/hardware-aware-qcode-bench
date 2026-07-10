from qiskit import QuantumCircuit
from qiskit.circuit.library import QFT

# Create a quantum circuit with 4 qubits (3 counting qubits and 1 target)
qc = QuantumCircuit(4)

# Prepare the eigenstate |1> on qubit 3
qc.x(3)

# Apply controlled powers of T gate
for counting_qubit in range(3):
    # The power is 2^counting_qubit
    power = 2 ** counting_qubit
    # Apply controlled-phase gate with phase pi/4 * power
    for _ in range(power):
        qc.cp(pi/4, counting_qubit, 3)

# Apply inverse QFT on counting qubits (0-2)
qft = QFT(3, inverse=True)
qc.append(qft, [0, 1, 2])