from qiskit import QuantumCircuit

qc = QuantumCircuit(4)
qc.h(0)  # Apply Hadamard to the first qubit
for qubit in range(1, 4):
    qc.cx(0, qubit)  # Apply CNOT from qubit 0 to qubits 1, 2, and 3