from qiskit import QuantumCircuit

# Create a quantum circuit with 8 qubits
qc = QuantumCircuit(8)

# Apply a Hadamard gate to the first qubit to create superposition
qc.h(0)

# Apply a series of CNOT gates to entangle all qubits in a GHZ state
for i in range(7):
    qc.cx(i, i + 1)