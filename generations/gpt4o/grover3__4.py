from qiskit import QuantumCircuit

# Create a QuantumCircuit with 3 qubits
qc = QuantumCircuit(3)

# Step 1: Apply Hadamard gates to all qubits to create a superposition
qc.h([0, 1, 2])

# Step 2: Oracle for the marked state |101>
# Mark the state |101> by applying a Z gate if the state is |101>
# This can be implemented using a combination of X, CCZ gates (controlled-Z with two controls)
qc.x(1)    # X on qubit 1 to flip it to |0>
qc.ccx(0, 2, 1)  # Controlled-Controlled-NOT (Toffoli) acts as controlled Z in this context
qc.x(1)    # X on qubit 1 to revert it back to |1>

# Step 3: Diffuser (inversion about the mean)
# Apply Hadamard gates to all qubits
qc.h([0, 1, 2])
# Apply X gates to all qubits
qc.x([0, 1, 2])
# Apply a multi-controlled Z gate (Z gate with three controls)
qc.h(2)    # Transform the multi-controlled Z to a multi-controlled X
qc.ccx(0, 1, 2)  # Toffoli gate (acts as a controlled-controlled Z when surrounded by Hadamards)
qc.h(2)    # Undo the transformation
# Apply X gates to all qubits
qc.x([0, 1, 2])
# Apply Hadamard gates to all qubits
qc.h([0, 1, 2])