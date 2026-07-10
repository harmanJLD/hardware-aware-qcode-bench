from qiskit import QuantumCircuit
from qiskit.circuit import Parameter

# Initialize quantum circuit with 4 qubits
qc = QuantumCircuit(4)

# Apply Hadamard gates to all qubits
qc.h([0, 1, 2, 3])

# Apply cost layer with gamma = 0.8
gamma = 0.8
qc.rzz(2 * gamma, 0, 1)  # Edge (0,1)
qc.rzz(2 * gamma, 1, 2)  # Edge (1,2)
qc.rzz(2 * gamma, 2, 3)  # Edge (2,3)
qc.rzz(2 * gamma, 3, 0)  # Edge (3,0)

# Apply mixer layer with beta = 0.4
beta = 0.4
qc.rx(2 * beta, 0)
qc.rx(2 * beta, 1)
qc.rx(2 * beta, 2)
qc.rx(2 * beta, 3)