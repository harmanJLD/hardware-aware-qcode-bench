from qiskit import QuantumCircuit

qc = QuantumCircuit(8)
qc.h(0)
for i in range(7):
    qc.cx(i, i+1)