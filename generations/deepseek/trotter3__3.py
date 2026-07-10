from qiskit import QuantumCircuit
from qiskit.circuit.library import RZZGate, RXGate

qc = QuantumCircuit(3)

# Apply RZZ(1.0) on qubits (0,1)
qc.append(RZZGate(1.0), [0, 1])

# Apply RZZ(1.0) on qubits (1,2)
qc.append(RZZGate(1.0), [1, 2])

# Apply RX(1.0) on each of the 3 qubits
for qubit in range(3):
    qc.append(RXGate(1.0), [qubit])