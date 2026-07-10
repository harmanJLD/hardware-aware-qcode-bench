from qiskit.circuit import QuantumCircuit

# Create a quantum circuit with 3 qubits
qc = QuantumCircuit(3)

# Apply the first RZZ gate
qc.rzz(1.0, 0, 1)

# Apply the second RZZ gate
qc.rzz(1.0, 1, 2)

# Apply the RX gates to all qubits
qc.rx(1.0, 0)
qc.rx(1.0, 1)
qc.rx(1.0, 2)