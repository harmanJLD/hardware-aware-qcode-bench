from qiskit import QuantumCircuit
from qiskit.circuit.library import RYGate

# Initialize the quantum circuit with 4 qubits
qc = QuantumCircuit(4)

# First layer of RY rotations
angles_layer_1 = [0.1, 0.2, 0.3, 0.4]
for qubit in range(4):
    qc.append(RYGate(angles_layer_1[qubit]), [qubit])

# First layer of CX gates
qc.cx(0, 1)
qc.cx(1, 2)
qc.cx(2, 3)

# Second layer of RY rotations
angles_layer_2 = [0.5, 0.6, 0.7, 0.8]
for qubit in range(4):
    qc.append(RYGate(angles_layer_2[qubit]), [qubit])

# Second layer of CX gates
qc.cx(0, 1)
qc.cx(1, 2)
qc.cx(2, 3)