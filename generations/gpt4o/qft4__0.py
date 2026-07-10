from qiskit import QuantumCircuit
from math import pi

def qft_dagger(n):
    """Creates an n-qubit QFTdagger circuit."""
    qc = QuantumCircuit(n)
    # Apply the QFT
    for qubit in range(n//2):
        qc.swap(qubit, n-qubit-1)
    for j in range(n):
        for m in range(j):
            qc.cp(-pi/float(2**(j-m)), m, j)
        qc.h(j)
    return qc

qc = QuantumCircuit(4)
# Apply the QFT to the circuit
qft_circuit = qft_dagger(4).inverse()
qc.append(qft_circuit, range(4))