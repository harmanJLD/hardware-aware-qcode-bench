from qiskit import QuantumCircuit

# Define the quantum circuit
qc = QuantumCircuit(3)

# Step 1: Apply Hadamard gates to all qubits
qc.h([0, 1, 2])

# Step 2: Phase Oracle for the marked state |101>
qc.cz(0, 2)  # Apply a controlled-Z gate (CZ) between qubit 0 and qubit 2
qc.x(1)      # Apply X gate to qubit 1 to flip it
qc.cz(1, 2)  # Apply another controlled-Z gate (CZ) between qubit 1 and qubit 2
qc.x(1)      # Apply X gate to qubit 1 to revert it back

# Step 3: Diffuser
qc.h([0, 1, 2])
qc.x([0, 1, 2])
qc.h(2)      # Apply Hadamard to qubit 2
qc.cz(0, 2)  # Apply controlled-Z between qubit 0 and qubit 2
qc.h(2)      # Apply Hadamard to qubit 2 again
qc.x([0, 1, 2])
qc.h([0, 1, 2])