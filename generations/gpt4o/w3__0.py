from qiskit import QuantumCircuit
from qiskit.circuit.library import XGate, RYGate, CRYGate

# Create a Quantum Circuit with 3 qubits
qc = QuantumCircuit(3)

# Apply the necessary gates to create the W state
qc.append(RYGate(2 * 1.2309594173407747), [0])  # RY(sin^-1(sqrt(1/3))) on qubit 0
qc.append(CRYGate(2 * 0.7227342478134157), [0, 1])  # CRY(sin^-1(sqrt(1/2))) from qubit 0 to qubit 1
qc.append(XGate(), [1])  # X gate on qubit 1
qc.append(CRYGate(-0.7227342478134157 * 2), [1, 2])  # CRY(-sin^-1(sqrt(1/2))) from qubit 1 to qubit 2
qc.append(XGate(), [2])  # X gate on qubit 2