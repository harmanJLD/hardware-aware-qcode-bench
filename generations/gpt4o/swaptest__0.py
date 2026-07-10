from qiskit import QuantumCircuit

# Create a QuantumCircuit with 3 qubits
qc = QuantumCircuit(3)

# Prepare the initial states
qc.x(1)        # Prepare qubit 1 in |1>
qc.h(2)        # Prepare qubit 2 in |+>

# Apply the SWAP test
qc.h(0)        # Apply H to the ancilla
qc.cswap(0, 1, 2)  # Controlled-SWAP with ancilla as control, swapping qubits 1 and 2
qc.h(0)        # Apply H to the ancilla again