from qiskit import QuantumCircuit

qc = QuantumCircuit(3)

qc.h(0)
qc.cx(0, 1)
qc.cx(0, 2)
qc.x(1)
qc.ccx(2, 1, 0)