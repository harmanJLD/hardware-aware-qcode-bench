from qiskit import QuantumCircuit

# Define a QuantumCircuit with 4 qubits
qc = QuantumCircuit(4)

# Apply the Quantum Fourier Transform
for j in range(4):
    qc.h(j)
    for k in range(j + 1, 4):
        qc.cp(np.pi / (2 ** (k - j)), k, j)

# Apply the final qubit-reversal SWAP gates
qc.swap(0, 3)
qc.swap(1, 2)