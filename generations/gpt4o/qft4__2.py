from qiskit import QuantumCircuit
from math import pi

def qft_rotations(circ, n):
    """Performs the basic phase shift rotations of the QFT on the first n qubits in circ."""
    if n == 0:
        return circ
    n -= 1
    circ.h(n)
    for qubit in range(n):
        circ.cu1(pi/2**(n-qubit), qubit, n)
    qft_rotations(circ, n)

def swap_registers(circ, n):
    """Swaps the qubits to reverse the order in the quantum register."""
    for qubit in range(n//2):
        circ.swap(qubit, n-qubit-1)
    return circ

def qft(circ, n):
    """Constructs the QFT on the first n qubits in circ."""
    qft_rotations(circ, n)
    swap_registers(circ, n)
    return circ

# Create a QuantumCircuit for 4 qubits
qc = QuantumCircuit(4)
qft(qc, 4)