from qiskit import QuantumCircuit
from qiskit.circuit import Parameter

# Define parameters
gamma = 0.8
beta = 0.4

# Create a quantum circuit with 4 qubits
qc = QuantumCircuit(4)

# Apply Hadamard gates to all qubits
qc.h(range(4))

# Apply the cost layer RZZ gates for each edge
qc.rzz(2 * gamma, 0, 1)
qc.rzz(2 * gamma, 1, 2)
qc.rzz(2 * gamma, 2, 3)
qc.rzz(2 * gamma, 3, 0)

# Apply the mixer RX gates to every qubit
qc.rx(2 * beta, 0)
qc.rx(2 * beta, 1)
qc.rx(2 * beta, 2)
qc.rx(2 * beta, 3)