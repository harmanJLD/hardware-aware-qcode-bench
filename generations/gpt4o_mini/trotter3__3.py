from qiskit import QuantumCircuit

qc = QuantumCircuit(3)

qc.rzz(1.0, 0, 1)
qc.rzz(1.0, 1, 2)
qc.rx(1.0, 0)
qc.rx(1.0, 1)
qc.rx(1.0, 2)