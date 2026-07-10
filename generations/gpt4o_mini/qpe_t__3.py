from qiskit import QuantumCircuit

# Create a Quantum Circuit with 4 qubits (3 counting qubits + 1 eigenstate qubit)
qc = QuantumCircuit(4)

# Prepare qubit 3 in the |1> state
qc.x(3)

# Apply Hadamard gates to the counting qubits (qubits 0, 1, 2)
for qubit in range(3):
    qc.h(qubit)

# Apply controlled-phase gates for the powers of T
# T gate is equivalent to a phase of π/4
# Controlled T (C-T) gates for the powers of T
qc.cp(3.14159 / 2, 0, 3)  # C-T^1
qc.cp(3.14159 / 4, 1, 3)  # C-T^2
qc.cp(3.14159 / 8, 2, 3)  # C-T^3

# Apply the inverse QFT
qc.swap(0, 2)  # Swap qubits 0 and 2
qc.h(0)        # Apply H to qubit 0
qc.cp(-3.14159 / 2, 1, 0)  # Controlled phase for qubit 1
qc.h(1)        # Apply H to qubit 1
qc.cp(-3.14159 / 4, 2, 1)  # Controlled phase for qubit 2
qc.h(2)        # Apply H to qubit 2

# The circuit is defined but no measurements are added