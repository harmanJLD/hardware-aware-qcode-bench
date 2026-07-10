from qiskit import QuantumCircuit

def qft_rotations(circuit, n):
    if n == 0:
        return circuit
    n -= 1
    circuit.h(n)
    for qubit in range(n):
        circuit.cp(pi/2**(n-qubit), qubit, n)

def swap_qubits(circuit, n):
    for qubit in range(n//2):
        circuit.swap(qubit, n-qubit-1)

n = 4
qc = QuantumCircuit(n)

# Apply QFT rotations
qft_rotations(qc, n)

# Apply SWAP gates for qubit reversal
swap_qubits(qc, n)