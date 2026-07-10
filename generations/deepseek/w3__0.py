from qiskit import QuantumCircuit

qc = QuantumCircuit(3)

qc.h(0)
qc.cx(0, 1)
qc.cx(0, 2)
qc.ch(1, 2)