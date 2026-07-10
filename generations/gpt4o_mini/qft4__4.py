from qiskit import QuantumCircuit

def quantum_fourier_transform(n):
    qc = QuantumCircuit(n)

    for j in range(n):
        # Apply Hadamard gate to the j-th qubit
        qc.h(j)
        for k in range(j + 1, n):
            # Apply controlled rotation gates
            qc.cu1(3.14159 / (2 ** (k - j)), k, j)

    # Add the reversal SWAP gates
    for j in range(n // 2):
        qc.swap(j, n - j - 1)

    return qc

qc = quantum_fourier_transform(4)