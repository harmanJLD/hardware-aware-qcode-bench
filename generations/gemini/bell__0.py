from qiskit import QuantumCircuit

# Create a quantum circuit with 2 qubits
qc = QuantumCircuit(2)

# Apply a Hadamard gate to the first qubit (qubit 0)
qc.h(0)

# Apply a CNOT gate with qubit 0 as the control and qubit 1 as the target
qc.cx(0, 1)