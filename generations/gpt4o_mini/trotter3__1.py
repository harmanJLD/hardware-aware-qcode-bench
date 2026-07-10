from qiskit import QuantumCircuit

# Create a QuantumCircuit with 3 qubits
qc = QuantumCircuit(3)

# Apply RZZ(1.0) on qubits (0, 1)
qc.rzz(1.0, 0, 1)

# Apply RZZ(1.0) on qubits (1, 2)
qc.rzz(1.0, 1, 2)

# Apply RX(1.0) on each of the 3 qubits
qc.rx(1.0, 0)
qc.rx(1.0, 1)
qc.rx(1.0, 2)