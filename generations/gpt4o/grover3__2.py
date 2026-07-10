from qiskit import QuantumCircuit

# Define the quantum circuit with 3 qubits
qc = QuantumCircuit(3)

# Apply Hadamard gates to all qubits
qc.h([0, 1, 2])

# Phase Oracle: Marks the state |101>
qc.x(1)  # Flip qubit 1 to turn |101> into |111>, making it recognizable by the multi-controlled Z
qc.ccx(0, 1, 2)  # Controlled-controlled-Z
qc.x(1)  # Flip qubit 1 back

# Apply Hadamard gates to all qubits for the diffuser
qc.h([0, 1, 2])

# Apply X gates to all qubits
qc.x([0, 1, 2])

# Apply multi-controlled Z (which is effectively a controlled-controlled-Z in this 3-qubit context)
qc.h(2)  # Convert the Z gate into an X gate by surrounding it with Hadamard gates
qc.ccx(0, 1, 2)
qc.h(2)

# Apply X gates to all qubits
qc.x([0, 1, 2])

# Apply Hadamard gates to all qubits again
qc.h([0, 1, 2])