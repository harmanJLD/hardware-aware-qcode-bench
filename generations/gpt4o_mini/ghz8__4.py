from qiskit import QuantumCircuit

# Define a QuantumCircuit object with 8 qubits
qc = QuantumCircuit(8)

# Create the GHZ state
qc.h(0)  # Apply Hadamard gate to the first qubit
for i in range(1, 8):
    qc.cx(0, i)  # Apply CNOT gates from the first qubit to the others