from qiskit.circuit import QuantumCircuit

# --- Define parameters ---
gamma = 0.8
beta = 0.4
n_qubits = 4
edges = [(0, 1), (1, 2), (2, 3), (3, 0)]

# --- Build the circuit ---
# Initialize the quantum circuit
qc = QuantumCircuit(n_qubits)

# 1. Initial state preparation: Apply Hadamard gates to all qubits
qc.h(range(n_qubits))

# 2. Cost layer: Apply RZZ gates for each edge
for u, v in edges:
    qc.rzz(2 * gamma, u, v)

# 3. Mixer layer: Apply RX gates to all qubits
qc.rx(2 * beta, range(n_qubits))