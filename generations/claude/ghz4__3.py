from qiskit import QuantumCircuit

qc = QuantumCircuit(4)

# Prepare GHZ state: (|0000> + |1111>)/sqrt(2)
qc.h(0)  # Apply Hadamard to first qubit
qc.cx(0, 1)  # CNOT from qubit 0 to qubit 1
qc.cx(0, 2)  # CNOT from qubit 0 to qubit 2
qc.cx(0, 3)  # CNOT from qubit 0 to qubit 3