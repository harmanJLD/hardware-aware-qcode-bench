from qiskit import QuantumCircuit
from math import pi

# Define a function to apply the quantum Fourier transform
def qft(circuit, n):
    """Apply the QFT on the first n qubits in the circuit."""
    for j in range(n):
        circuit.h(j)
        for k in range(j+1, n):
            circuit.cp(pi/float(2**(k-j)), k, j)
        
# Define a function to apply the qubit reversal swap gates
def swap_registers(circuit, n):
    """Swap the qubits to reverse the order for QFT."""
    for i in range(n//2):
        circuit.swap(i, n-i-1)

# Create a quantum circuit with 4 qubits
qc = QuantumCircuit(4)

# Apply QFT on all 4 qubits
qft(qc, 4)

# Apply swap gates to reverse qubit order
swap_registers(qc, 4)