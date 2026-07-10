from qiskit import QuantumCircuit

# Initialize a QuantumCircuit with 3 qubits
qc = QuantumCircuit(3)

# Apply Hadamard gates to all qubits to create superposition
qc.h(range(3))

# Phase oracle for the marked state |101>
qc.cz(0, 2)  # Apply CZ gate on qubits 0 and 2
qc.x(1)      # Apply X gate on qubit 1 to flip it to |1>
qc.cz(0, 2)  # Apply CZ gate on qubits 0 and 2 again
qc.x(1)      # Apply X gate on qubit 1 to flip it back to |0>

# Diffuser (Grover's diffusion operator)
qc.h(range(3))
qc.x(range(3))
qc.h(2)
qc.cz(0, 2)
qc.h(2)
qc.x(range(3))
qc.h(range(3))