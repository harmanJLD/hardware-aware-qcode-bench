from qiskit import QuantumCircuit
from qiskit.circuit import Parameter

# Initialize quantum circuit with 4 qubits
qc = QuantumCircuit(4)

# Apply Hadamard gates to all qubits
qc.h([0, 1, 2, 3])

# Cost layer with gamma = 0.8
gamma = 0.8
# Apply RZZ gates for each edge in order (0,1), (1,2), (2,3), (3,0)
qc.rzz(2 * gamma, 0, 1)
qc.rzz(2 * gamma, 1, 2)
qc.rzz(2 * gamma, 2, 3)
qc.rzz(2 * gamma, 3, 0)

# Mixer layer with beta = 0.4
beta = 0.4
# Apply RX gates to all qubits
qc.rx(2 * beta, 0)
qc.rx(2 * beta, 1)
qc.rx(2 * beta, 2)
qc.rx(2 * beta, 3)