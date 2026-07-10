from qiskit import QuantumCircuit

qc = QuantumCircuit(8)

# Prepare 8-qubit GHZ state
qc.h(0)  # Apply Hadamard to first qubit
for i in range(7):
    qc.cx(i, i+1)  # Apply CNOT gates to entangle all qubits