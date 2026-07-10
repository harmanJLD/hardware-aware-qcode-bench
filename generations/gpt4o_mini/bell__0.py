from qiskit import QuantumCircuit

qc = QuantumCircuit(2)
qc.h(0)  # Apply Hadamard gate to the first qubit
qc.cx(0, 1)  # Apply CNOT gate with the first qubit as control and the second as target