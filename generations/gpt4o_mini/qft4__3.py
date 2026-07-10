from qiskit import QuantumCircuit

# Define the quantum circuit for the 4-qubit quantum Fourier transform
qc = QuantumCircuit(4)

# Apply the QFT
for j in range(4):
    qc.h(j)
    for k in range(j + 1, 4):
        qc.cp(3.141592653589793 / (2 ** (k - j)), k, j)

# Final qubit-reversal SWAP gates
qc.swap(0, 3)
qc.swap(1, 2)