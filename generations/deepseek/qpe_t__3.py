from qiskit import QuantumCircuit
from qiskit.circuit.library import QFT

# Create a QuantumCircuit with 4 qubits (3 counting qubits and 1 target qubit)
qc = QuantumCircuit(4)

# Prepare the target qubit (qubit 3) in the eigenstate |1>
qc.x(3)

# Apply controlled-T gates with powers corresponding to the counting qubits
qc.cp(3.141592653589793 / 4, 0, 3)  # Controlled-T (T^1)
qc.cp(3.141592653589793 / 2, 1, 3)  # Controlled-T^2
qc.cp(3.141592653589793, 2, 3)      # Controlled-T^4

# Apply the inverse QFT to the counting register (qubits 0-2)
qft_circuit = QFT(3, inverse=True)
qc.compose(qft_circuit, qubits=[0, 1, 2], inplace=True)