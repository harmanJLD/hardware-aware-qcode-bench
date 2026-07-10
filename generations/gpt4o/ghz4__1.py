from qiskit import QuantumCircuit

# Create a quantum circuit with 4 qubits
qc = QuantumCircuit(4)

# Apply a Hadamard gate to the first qubit
qc.h(0)

# Apply CNOT gates to entangle the qubits
qc.cx(0, 1)
qc.cx(1, 2)
qc.cx(2, 3)