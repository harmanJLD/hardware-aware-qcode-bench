from qiskit import QuantumCircuit

# Create a 3-qubit quantum circuit
qc = QuantumCircuit(3)

# Initial Hadamard gates on all qubits
qc.h([0, 1, 2])

# Phase oracle for |101> (qubit 0=1, qubit 1=0, qubit 2=1)
qc.cz(0, 2)  # This flips the phase of |101> since:
              # - qubit 0 is control (must be 1)
              # - qubit 2 is target (must be 1)
              # - qubit 1 is 0 (no action needed)

# Diffusion operator
qc.h([0, 1, 2])
qc.x([0, 1, 2])
qc.h(2)
qc.ccx(0, 1, 2)
qc.h(2)
qc.x([0, 1, 2])
qc.h([0, 1, 2])