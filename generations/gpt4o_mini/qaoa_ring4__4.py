from qiskit import QuantumCircuit
from qiskit.circuit import Parameter

# Define parameters
gamma = 0.8
beta = 0.4

# Create a QuantumCircuit with 4 qubits
qc = QuantumCircuit(4)

# Apply Hadamard gates to all qubits
qc.h([0, 1, 2, 3])

# Apply cost layer for each edge
qc.rzz(2 * gamma, 0, 1)  # For edge (0, 1)
qc.rzz(2 * gamma, 1, 2)  # For edge (1, 2)
qc.rzz(2 * gamma, 2, 3)  # For edge (2, 3)
qc.rzz(2 * gamma, 3, 0)  # For edge (3, 0)

# Apply mixer layer
qc.rx(2 * beta, [0, 1, 2, 3])