from qiskit import QuantumCircuit

qc = QuantumCircuit(8)
qc.h(0)  # Apply Hadamard gate to the first qubit
for i in range(1, 8):
    qc.cx(0, i)  # Apply CNOT gates to entangle the rest of the qubits