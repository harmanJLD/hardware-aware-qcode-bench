from qiskit import QuantumCircuit
from qiskit.circuit.library import RZZGate, RXGate

# Define parameters gamma and beta
gamma = 0.8
beta = 0.4

# Create a quantum circuit with 4 qubits
qc = QuantumCircuit(4)

# Apply Hadamard gates to all qubits
qc.h(range(4))

# Apply the cost layer using RZZ gates for each edge
edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
for a, b in edges:
    qc.append(RZZGate(2 * gamma), [a, b])

# Apply the mixer layer using RX gates
for qubit in range(4):
    qc.rx(2 * beta, qubit)