from qiskit import QuantumCircuit

def qft_rotations(circuit, n):
    """Performs the QFT rotations on the first n qubits in the circuit."""
    if n == 0:
        return circuit
    n -= 1
    circuit.h(n)
    for qubit in range(n):
        circuit.cp(np.pi/2**(n-qubit), qubit, n)

def swap_qubits(circuit, n):
    """Swaps the qubits to reverse the order."""
    for qubit in range(n//2):
        circuit.swap(qubit, n-qubit-1)

def qft(circuit, n):
    """QFT on the first n qubits in the circuit, including SWAPs for qubit reversal."""
    qft_rotations(circuit, n)
    swap_qubits(circuit, n)

# Create a 4-qubit quantum circuit
qc = QuantumCircuit(4)

# Apply QFT to all 4 qubits
qft(qc, 4)