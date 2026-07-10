from qiskit import QuantumCircuit

# Define the quantum circuit with 5 qubits
qc = QuantumCircuit(5)

# First RY rotation layer
qc.ry(0.1, 0)
qc.ry(0.2, 1)
qc.ry(0.3, 2)
qc.ry(0.4, 3)
qc.ry(0.5, 4)

# Circular CX entanglement
qc.cx(0, 1)
qc.cx(1, 2)
qc.cx(2, 3)
qc.cx(3, 4)
qc.cx(4, 0)

# Second RY rotation layer
qc.ry(0.6, 0)
qc.ry(0.7, 1)
qc.ry(0.8, 2)
qc.ry(0.9, 3)
qc.ry(1.0, 4)