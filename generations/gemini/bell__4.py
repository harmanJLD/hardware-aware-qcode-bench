from qiskit import QuantumCircuit

# Create a quantum circuit with 2 qubits
qc = QuantumCircuit(2)

# Apply a Hadamard gate to the first qubit to create superposition
qc.h(0)

# Apply a CNOT gate with the first qubit as control and the second as target
# This entangles the two qubits
qc.cnot(0, 1)