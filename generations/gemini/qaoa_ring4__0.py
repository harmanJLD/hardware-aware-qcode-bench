from qiskit import QuantumCircuit

# Parameters for the QAOA circuit
gamma = 0.8
beta = 0.4
num_qubits = 4

# Create the QuantumCircuit object
qc = QuantumCircuit(num_qubits)

# 1. Initial state: Apply Hadamards to all qubits
qc.h(range(num_qubits))

# 2. Cost layer: Apply RZZ gates for each edge in the ring graph
# Edges are (0,1), (1,2), (2,3), (3,0)
qc.rzz(2 * gamma, 0, 1)
qc.rzz(2 * gamma, 1, 2)
qc.rzz(2 * gamma, 2, 3)
qc.rzz(2 * gamma, 3, 0)

# 3. Mixer layer: Apply RX gates to all qubits
qc.rx(2 * beta, range(num_qubits))