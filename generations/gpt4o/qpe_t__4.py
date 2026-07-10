from qiskit import QuantumCircuit
from qiskit.circuit.library import QFT

# Create a Quantum Circuit with 4 qubits
qc = QuantumCircuit(4)

# Prepare qubit 3 in the |1> state (eigenstate of the T gate)
qc.x(3)

# Apply Hadamard gates to the counting qubits (qubits 0-2)
qc.h(0)
qc.h(1)
qc.h(2)

# Controlled unitary operations (controlled powers of the T gate)
qc.cp(1/8 * 2 * 3.141592653589793, 0, 3) # T^1 = T
qc.cp(1/4 * 2 * 3.141592653589793, 1, 3) # T^2
qc.cp(1/2 * 2 * 3.141592653589793, 2, 3) # T^4

# Apply the inverse QFT on the counting qubits (qubits 0-2)
qft_dagger = QFT(3, inverse=True, do_swaps=True)
qc.append(qft_dagger, [0, 1, 2])