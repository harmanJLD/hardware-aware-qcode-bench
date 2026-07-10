from qiskit import QuantumCircuit
from qiskit.circuit.library import QFT

# Create a quantum circuit with 4 qubits (3 counting qubits and 1 target qubit)
qc = QuantumCircuit(4)

# Prepare the eigenstate |1> on qubit 3
qc.x(3)

# Apply controlled-phase gates for the controlled powers of T gate
# T gate phase is pi/4, so controlled-T^k has phase k*pi/4
for counting_qubit in range(3):
    for _ in range(2 ** counting_qubit):
        # Controlled-phase gate with phase pi/4 (T gate)
        # Target is qubit 3, control is the current counting qubit
        qc.cp(3.141592653589793 / 4, counting_qubit, 3)

# Apply inverse QFT on the counting register (qubits 0-2)
qft = QFT(3, inverse=True, do_swaps=True)
qc.compose(qft, qubits=[0, 1, 2], inplace=True)