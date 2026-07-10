from qiskit import QuantumCircuit

# Define the QuantumCircuit object
qc = QuantumCircuit(3)

# Apply Hadamard gates to all qubits
qc.h(range(3))

# Phase oracle for the balanced function f(x) = x0 XOR x1
qc.cx(0, 2)  # CNOT gate from qubit 0 to qubit 2
qc.cx(1, 2)  # CNOT gate from qubit 1 to qubit 2

# Apply Hadamard gates to all qubits again
qc.h(range(3))