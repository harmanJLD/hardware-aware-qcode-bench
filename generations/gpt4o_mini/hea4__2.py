from qiskit import QuantumCircuit
import numpy as np

# Define the quantum circuit with 4 qubits
qc = QuantumCircuit(4)

# Layer 1: Apply RY gates
qc.ry(0.1, 0)
qc.ry(0.2, 1)
qc.ry(0.3, 2)
qc.ry(0.4, 3)

# Layer 1: Apply CX gates
qc.cx(0, 1)
qc.cx(1, 2)
qc.cx(2, 3)

# Layer 2: Apply RY gates
qc.ry(0.5, 0)
qc.ry(0.6, 1)
qc.ry(0.7, 2)
qc.ry(0.8, 3)

# Layer 2: Apply CX gates
qc.cx(0, 1)
qc.cx(1, 2)
qc.cx(2, 3)