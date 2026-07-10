from qiskit import QuantumCircuit

# Create a QuantumCircuit with 5 qubits
qc = QuantumCircuit(5)

# Apply X gates to qubits 1, 2, and 4 to set them to |1>
qc.x(1)
qc.x(2)
qc.x(4)