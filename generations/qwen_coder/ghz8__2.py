from qiskit import QuantumCircuit

qc = QuantumCircuit(8)
qc.h(0)
for i in range(1, 8):
    qc.cx(0, i)