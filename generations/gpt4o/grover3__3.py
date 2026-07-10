from qiskit import QuantumCircuit
from qiskit.circuit.library import ZGate, HGate, XGate

# Create a QuantumCircuit with 3 qubits
qc = QuantumCircuit(3)

# Apply Hadamard gates to all qubits to create the superposition
qc.h(range(3))

# Phase oracle that marks the state |101>
qc.x(0)
qc.x(1)
qc.x(2)
qc.h(2)
qc.mcx([0, 1], 2)  # Controlled-Z gate, with qubit 2 as the target
qc.h(2)
qc.x(0)
qc.x(1)
qc.x(2)

# Diffuser (inversion about the mean)
qc.h(range(3))
qc.x(range(3))
qc.h(2)
qc.mcx([0, 1], 2)  # Controlled-Z gate, with qubit 2 as the target
qc.h(2)
qc.x(range(3))
qc.h(range(3))