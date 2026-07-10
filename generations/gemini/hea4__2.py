from qiskit import QuantumCircuit

# Initialize a 4-qubit quantum circuit
qc = QuantumCircuit(4)

# --- Layer 1 ---
# Apply RY gates with the specified angles
qc.ry(0.1, 0)
qc.ry(0.2, 1)
qc.ry(0.3, 2)
qc.ry(0.4, 3)
# Apply the linear entanglement
qc.cx(0, 1)
qc.cx(1, 2)
qc.cx(2, 3)

# --- Layer 2 ---
# Apply RY gates with the specified angles
qc.ry(0.5, 0)
qc.ry(0.6, 1)
qc.ry(0.7, 2)
qc.ry(0.8, 3)
# Apply the linear entanglement
qc.cx(0, 1)
qc.cx(1, 2)
qc.cx(2, 3)