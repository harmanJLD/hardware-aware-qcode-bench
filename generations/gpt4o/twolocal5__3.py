from qiskit import QuantumCircuit

# Create a quantum circuit with 5 qubits
qc = QuantumCircuit(5)

# First RY rotation layer
angles1 = [0.1, 0.2, 0.3, 0.4, 0.5]
for i in range(5):
    qc.ry(angles1[i], i)

# Circular CX entanglement
qc.cx(0, 1)
qc.cx(1, 2)
qc.cx(2, 3)
qc.cx(3, 4)
qc.cx(4, 0)

# Second RY rotation layer
angles2 = [0.6, 0.7, 0.8, 0.9, 1.0]
for i in range(5):
    qc.ry(angles2[i], i)