from qiskit import QuantumCircuit
import numpy as np

def qft_dagger(n):
    """Creates the inverse of the QFT on n qubits."""
    qc = QuantumCircuit(n)
    for qubit in range(n//2):
        qc.swap(qubit, n-qubit-1)
    for j in range(n):
        for k in range(j):
            qc.cp(-np.pi/2**(j-k), k, j)
        qc.h(j)
    return qc

qc = qft_dagger(4)
qc = qc.inverse()