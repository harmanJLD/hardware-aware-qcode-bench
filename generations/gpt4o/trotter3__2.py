from qiskit import QuantumCircuit
from qiskit.circuit.library import RZZGate, RXGate

# Initialize the QuantumCircuit with 3 qubits
qc = QuantumCircuit(3)

# Apply RZZ(1.0) gate on qubits (0, 1)
qc.append(RZZGate(1.0), [0, 1])

# Apply RZZ(1.0) gate on qubits (1, 2)
qc.append(RZZGate(1.0), [1, 2])

# Apply RX(1.0) gate on each of the 3 qubits
qc.append(RXGate(1.0), [0])
qc.append(RXGate(1.0), [1])
qc.append(RXGate(1.0), [2])