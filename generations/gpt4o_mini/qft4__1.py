from qiskit import QuantumCircuit

# Create a Quantum Circuit with 4 qubits
qc = QuantumCircuit(4)

# Apply the Quantum Fourier Transform (QFT)
def qft(qc, n):
    for j in range(n):
        qc.h(j)
        for k in range(j+1, n):
            qc.cp(np.pi / (2 ** (k - j)), k, j)
    
    # Swap the qubits to reverse their order
    for j in range(n // 2):
        qc.swap(j, n - j - 1)

# Execute QFT on 4 qubits
qft(qc, 4)