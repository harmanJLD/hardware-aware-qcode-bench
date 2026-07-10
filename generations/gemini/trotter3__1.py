from qiskit.circuit import QuantumCircuit

# Create a quantum circuit with 3 qubits
qc = QuantumCircuit(3)

# Apply the first-order Trotter step
# RZZ(1.0) on qubits (0,1)
qc.rzz(1.0, 0, 1)

# RZZ(1.0) on qubits (1,2)
qc.rzz(1.0, 1, 2)

# RX(1.0) on each qubit
qc.rx(1.0, 0)
qc.rx(1.0, 1)
qc.rx(1.0, 2)