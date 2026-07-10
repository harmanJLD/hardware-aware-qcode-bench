```python
from qiskit import QuantumCircuit
import math

def qft_rotations(circuit, n):
    "Performs qft on the first n qubits in circuit (without swaps)"""
    if n == 0:
        return circuit
    n -= 1
    circuit.h(n)
    for qubit in range(n):
        circuit.cu1(math.pi/2**(n-qubit), qubit, n)
    qft_rotations(circuit, n)

qc = QuantumCircuit(4)
qft_rotations(qc,