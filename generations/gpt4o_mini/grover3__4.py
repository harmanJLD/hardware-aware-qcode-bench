from qiskit import QuantumCircuit

# Create a QuantumCircuit with 3 qubits
qc = QuantumCircuit(3)

# Step 1: Apply Hadamard gates to all qubits
qc.h([0, 1, 2])

# Step 2: Phase oracle for the marked state |101>
qc.x([0, 1])  # Prepare |110>
qc.ccx(0, 1, 2)  # Apply Toffoli gate
qc.x([0, 1])  # Revert to |101>

# Step 3: Apply Hadamard gates to all qubits again
qc.h([0, 1, 2])

# Step 4: Apply the diffuser
qc.x([0, 1, 2])  # Apply X gates
qc.h(2)  # Apply H gate to the last qubit
qc.cz(1, 2)  # Apply CZ gate
qc.h(2)  # Apply H gate to the last qubit
qc.x([0, 1, 2])  # Apply X gates again

# The circuit is now ready for one iteration of Grover's algorithm