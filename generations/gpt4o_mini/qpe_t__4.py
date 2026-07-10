from qiskit import QuantumCircuit
from qiskit.circuit.library import QFT

# Create a QuantumCircuit with 4 qubits (3 counting qubits and 1 eigenstate qubit)
qc = QuantumCircuit(4)

# Prepare qubit 3 in |1> state
qc.x(3)

# Apply Hadamard gates to the counting qubits
qc.h([0, 1, 2])

# Controlled phase gates for powers of T gate
qc.append(qc.t, [3]).control(1).append(qc.t, [3]).control(2).append(qc.t, [3]).control(3)

# Apply the inverse QFT
qft = QFT(3, inverse=True)
qc.append(qft, [0, 1, 2])

# The circuit is now complete