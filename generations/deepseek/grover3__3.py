from qiskit import QuantumCircuit

# Create a quantum circuit with 3 qubits
qc = QuantumCircuit(3)

# Initial Hadamard gates on all qubits
qc.h([0, 1, 2])

# Phase oracle for |101⟩ (qubit 0=1, qubit 1=0, qubit 2=1)
qc.cz(0, 2)  # This flips the phase of |101⟩ since qubit 1 is |0⟩ in the target state
qc.x(1)      # Flip qubit 1 to apply CZ conditionally on |1⟩
qc.cz(0, 2)  # This cancels the phase flip for all states except |101⟩
qc.x(1)      # Flip qubit 1 back

# Diffuser (inversion about the average)
qc.h([0, 1, 2])
qc.x([0, 1, 2])
qc.h(2)
qc.ccx(0, 1, 2)
qc.h(2)
qc.x([0, 1, 2])
qc.h([0, 1, 2])