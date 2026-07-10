from qiskit import QuantumCircuit

qc = QuantumCircuit(5)
qc.x([1, 2, 4])  # Apply X gates to qubits 1, 2, and 4 to set them to |1>