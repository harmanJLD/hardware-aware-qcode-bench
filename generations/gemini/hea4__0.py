from qiskit.circuit import QuantumCircuit

# Define the number of qubits
num_qubits = 4

# Create a Quantum Circuit
qc = QuantumCircuit(num_qubits)

# --- Layer 1 ---
# Apply single-qubit rotation gates
qc.ry(0.1, 0)
qc.ry(0.2, 1)
qc.ry(0.3, 2)
qc.ry(0.4, 3)

# Apply entangling gates
qc.cx(0, 1)
qc.cx(1, 2)
qc.cx(2, 3)

# --- Layer 2 ---
# Apply single-qubit rotation gates
qc.ry(0.5, 0)
qc.ry(0.6, 1)
qc.ry(0.7, 2)
qc.ry(0.8, 3)

# Apply entangling gates
qc.cx(0, 1)
qc.cx(1, 2)
qc.cx(2, 3)