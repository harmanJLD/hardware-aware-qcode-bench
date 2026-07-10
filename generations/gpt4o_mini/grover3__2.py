from qiskit import QuantumCircuit

# Define the quantum circuit with 3 qubits
qc = QuantumCircuit(3)

# Step 1: Apply Hadamard gates to all qubits
qc.h([0, 1, 2])

# Step 2: Apply the phase oracle for the marked state |101>
qc.z(0)  # Apply Z gate to qubit 0
qc.z(2)  # Apply Z gate to qubit 2

# Step 3: Apply the diffuser
qc.h([0, 1, 2])
qc.x([0, 1, 2])
qc.h(2)
qc.cz(0, 2)
qc.h(2)
qc.x([0, 1, 2])
qc.h([0, 1, 2])