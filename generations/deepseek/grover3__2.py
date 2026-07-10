from qiskit import QuantumCircuit

# Create a quantum circuit with 3 qubits
qc = QuantumCircuit(3)

# Initial Hadamard gates to create superposition
qc.h([0, 1, 2])

# Phase oracle for the state |101⟩ (qubit 0=1, qubit 1=0, qubit 2=1)
# This marks the state |101⟩ with a -1 phase
qc.cz(0, 2)  # This flips the phase of |101⟩ since |1⟩ is controlled
qc.x(1)      # To make the middle qubit act as |0⟩ control
qc.cz(0, 2)  # Apply CZ again (undoing the previous one for other states)
qc.x(1)      # Return the middle qubit to original state

# Diffuser (inversion about the average)
qc.h([0, 1, 2])
qc.x([0, 1, 2])
qc.h(2)
qc.ccx(0, 1, 2)
qc.h(2)
qc.x([0, 1, 2])
qc.h([0, 1, 2])