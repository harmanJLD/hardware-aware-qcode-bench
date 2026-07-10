from qiskit import QuantumCircuit

qc = QuantumCircuit(2)
qc.h()
qc.cx(0, 1)