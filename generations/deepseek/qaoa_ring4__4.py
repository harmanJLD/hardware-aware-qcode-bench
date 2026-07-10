from qiskit import QuantumCircuit
from qiskit.circuit.library import RZZGate, RXGate

# Initialize the QuantumCircuit with 4 qubits
qc = QuantumCircuit(4)

# Apply Hadamard gates to all qubits
qc.h(range(4))

# Define gamma and beta
gamma = 0.8
beta = 0.4

# Apply the cost layer: RZZ(2*gamma) for each edge
edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
for (a, b) in edges:
    qc.append(RZZGate(2 * gamma), [a, b])

# Apply the mixer layer: RX(2*beta) to every qubit
qc.rx(2 * beta, range(4))