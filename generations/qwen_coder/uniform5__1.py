from qiskit import QuantumCircuit

qc = QuantumCircuit(5)
for qubit in range(5):
    qc.h(qubit)