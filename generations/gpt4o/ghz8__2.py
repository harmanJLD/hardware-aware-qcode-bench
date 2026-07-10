from qiskit import QuantumCircuit

# Create a Quantum Circuit with 8 qubits
qc = QuantumCircuit(8)

# Apply a Hadamard gate to the first qubit
qc.h(0)

# Apply a series of CNOT gates to create the GHZ state
for i in range(7):
    qc.cx(i, i+1)