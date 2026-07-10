from qiskit.circuit import QuantumCircuit

# Define the number of qubits and rotation angles
num_qubits = 5
ry_params1 = [0.1, 0.2, 0.3, 0.4, 0.5]
ry_params2 = [0.6, 0.7, 0.8, 0.9, 1.0]

# Create a QuantumCircuit object
qc = QuantumCircuit(num_qubits)

# First RY rotation layer
for i, angle in enumerate(ry_params1):
    qc.ry(angle, i)

# Circular CX entanglement layer
for i in range(num_qubits):
    control_qubit = i
    target_qubit = (i + 1) % num_qubits
    qc.cx(control_qubit, target_qubit)

# Second RY rotation layer
for i, angle in enumerate(ry_params2):
    qc.ry(angle, i)