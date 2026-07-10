from qiskit import QuantumCircuit
from qiskit.circuit.library import RYGate

# Create a QuantumCircuit with 4 qubits
qc = QuantumCircuit(4)

# Layer 1: RY gates followed by CX gates
ry_angles_layer1 = [0.1, 0.2, 0.3, 0.4]
for i, angle in enumerate(ry_angles_layer1):
    qc.append(RYGate(angle), [i])

# CX gates for layer 1
qc.cx(0, 1)
qc.cx(1, 2)
qc.cx(2, 3)

# Layer 2: RY gates followed by CX gates
ry_angles_layer2 = [0.5, 0.6, 0.7, 0.8]
for i, angle in enumerate(ry_angles_layer2):
    qc.append(RYGate(angle), [i])

# CX gates for layer 2
qc.cx(0, 1)
qc.cx(1, 2)
qc.cx(2, 3)