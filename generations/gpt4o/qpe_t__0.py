from qiskit import QuantumCircuit
from qiskit.circuit.library import QFT

# Create a QuantumCircuit with 4 qubits
qc = QuantumCircuit(4)

# Prepare the eigenstate |1> on qubit 3
qc.x(3)

# Apply Hadamard gates to the counting qubits (qubits 0-2)
qc.h(0)
qc.h(1)
qc.h(2)

# Implement the controlled-phase operations
# Controlled T gate (T = U1(pi/4)), T^1 = T
qc.cp(pi/4, 0, 3)

# Controlled T^2 gate (T^2 = U1(pi/2))
qc.cp(pi/2, 1, 3)

# Controlled T^4 gate (T^4 = U1(pi)), note: T^4 = S = sqrt(Z)
qc.cp(pi, 2, 3)

# Apply the inverse QFT on the counting register
qft_dagger = QFT(3, inverse=True, do_swaps=True)
qc.append(qft_dagger, [0, 1, 2])