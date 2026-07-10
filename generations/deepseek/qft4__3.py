from qiskit import QuantumCircuit

def qft_rotations(qc, n):
    if n == 0:
        return
    n -= 1
    qc.h(n)
    for qubit in range(n):
        qc.cp(pi/2**(n-qubit), qubit, n)

def swap_registers(qc, n):
    for qubit in range(n//2):
        qc.swap(qubit, n-qubit-1)

def qft(qc, n):
    qft_rotations(qc, n)
    swap_registers(qc, n)

# Create a 4-qubit quantum circuit
qc = QuantumCircuit(4)
qft(qc, 4)