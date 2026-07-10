from qiskit import QuantumCircuit
from qiskit.circuit.library import Initialize

# Define the 3-qubit W state
w_state = [1/3**0.5, 0, 1/3**0.5, 0, 1/3**0.5, 0, 0, 0]

# Create a QuantumCircuit object
qc = QuantumCircuit(3)

# Initialize the circuit to the W state
qc.append(Initialize(w_state), [0, 1, 2])