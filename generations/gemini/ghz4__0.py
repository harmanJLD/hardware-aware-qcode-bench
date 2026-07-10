from qiskit import QuantumCircuit

# Create a Quantum Circuit with 4 qubits
qc = QuantumCircuit(4)

# Put the first qubit in superposition
qc.h(0)

# Create entanglement using CNOT gates
qc.cx(0, 1)
qc.cx(0, 2)
qc.cx(0, 3)