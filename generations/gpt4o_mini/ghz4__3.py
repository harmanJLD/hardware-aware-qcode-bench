from qiskit import QuantumCircuit

qc = QuantumCircuit(4)
qc.h(0)  # Apply Hadamard to the first qubit
qc.cx(0, 1)  # Apply CNOT from qubit 0 to qubit 1
qc.cx(0, 2)  # Apply CNOT from qubit 0 to qubit 2
qc.cx(0, 3)  # Apply CNOT from qubit 0 to qubit 3