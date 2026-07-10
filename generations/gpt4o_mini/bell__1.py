from qiskit import QuantumCircuit

qc = QuantumCircuit(2)
qc.h(0)  # Apply Hadamard gate to the first qubit
qc.cx(0, 1)  # Apply CNOT gate with control qubit 0 and target qubit 1