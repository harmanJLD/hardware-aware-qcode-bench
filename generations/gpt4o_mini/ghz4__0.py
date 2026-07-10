from qiskit import QuantumCircuit

qc = QuantumCircuit(4)
qc.h(0)  # Apply Hadamard gate to the first qubit
for i in range(1, 4):
    qc.cx(0, i)  # Apply CNOT gates to create entanglement