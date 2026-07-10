from qiskit import QuantumCircuit

# Create a Quantum Circuit with 2 qubits
qc = QuantumCircuit(2)

# Apply a Hadamard gate on the first qubit
qc.h(0)

# Apply a CNOT gate with the first qubit as control and second qubit as target
qc.cx(0, 1)