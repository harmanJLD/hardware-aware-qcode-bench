from qiskit import QuantumCircuit

# Create a quantum circuit with 5 qubits
qc = QuantumCircuit(5)

# Apply X gates to flip qubits 1, 2, and 4 to the |1> state
qc.x(1)
qc.x(2)
qc.x(4)