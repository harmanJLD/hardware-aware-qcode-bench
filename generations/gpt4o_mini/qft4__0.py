from qiskit import QuantumCircuit

qc = QuantumCircuit(4)

# Apply Hadamard gates to the first qubit
qc.h(0)

# Apply controlled rotations
qc.cp(pi/2, 1, 0)
qc.cp(pi/4, 2, 0)
qc.cp(pi/8, 3, 0)

qc.h(1)
qc.cp(pi/2, 2, 1)
qc.cp(pi/4, 3, 1)

qc.h(2)
qc.cp(pi/2, 3, 2)

qc.h(3)

# Apply the SWAP gates for qubit reversal
qc.swap(0, 3)
qc.swap(1, 2)