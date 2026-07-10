from qiskit import QuantumCircuit

# Define the QAOA parameters
gamma = 0.8
beta = 0.4

# Initialize a 4-qubit quantum circuit
qc = QuantumCircuit(4)

# 1. Start with Hadamards on all qubits to create the uniform superposition
qc.h(range(4))

# 2. Apply the cost layer for the ring graph edges
# Edges: (0,1), (1,2), (2,3), (3,0)
qc.rzz(2 * gamma, 0, 1)
qc.rzz(2 * gamma, 1, 2)
qc.rzz(2 * gamma, 2, 3)
qc.rzz(2 * gamma, 3, 0)

# 3. Apply the mixer layer
qc.rx(2 * beta, range(4))