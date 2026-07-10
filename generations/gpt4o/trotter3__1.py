from qiskit import QuantumCircuit
from qiskit.circuit.library import RZZGate, RXGate

qc = QuantumCircuit(3)
qc.append(RZZGate(1.0), [0, 1])
qc.append(RZZGate(1.0), [1, 2])
qc.append(RXGate(1.0), [0])
qc.append(RXGate(1.0), [1])
qc.append(RXGate(1.0), [2])