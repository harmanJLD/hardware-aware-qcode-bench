from qiskit import QuantumCircuit

# Define the QuantumCircuit
qc = QuantumCircuit(3)

# Step 1: Apply Hadamard gates to all qubits
qc.h([0, 1, 2])

# Step 2: Phase Oracle for the marked state |101>
qc.x([0, 1])  # Flip qubits 0 and 1
qc.ccx(0, 1, 2)  # CNOT between qubits 0, 1 and 2
qc.x([0, 1])  # Flip back qubits 0 and 1

# Step 3: Apply Hadamard gates to the last qubit before the diffuser
qc.h([0, 1, 2])
qc.x([0, 1, 2])
qc.h(2)
qc.ccx(0, 1, 2)
qc.h(2)
qc.x([0, 1, 2])
qc.h([0, 1, 2])