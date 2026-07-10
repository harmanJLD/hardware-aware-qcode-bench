from qiskit import QuantumCircuit
from qiskit.circuit.library import RZZ

# Define parameters
gamma = 0.8
beta = 0.4

# Create a QuantumCircuit with 4 qubits
qc = QuantumCircuit(4)

# Apply Hadamard gates to all qubits
qc.h([0, 1, 2, 3])

# Apply the cost layer RZZ gates for each edge
qc.append(RZZ(2 * gamma), [0, 1])  # for edge (0,1)
qc.append(RZZ(2 * gamma), [1, 2])  # for edge (1,2)
qc.append(RZZ(2 * gamma), [2, 3])  # for edge (2,3)
qc.append(RZZ(2 * gamma), [3, 0])  # for edge (3,0)

# Apply the mixer layer RX gates to all qubits
qc.rx(2 * beta, [0, 1, 2, 3])