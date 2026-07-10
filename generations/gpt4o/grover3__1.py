from qiskit import QuantumCircuit
from qiskit.circuit.library import ZGate, HGate, XGate

# Define the number of qubits
num_qubits = 3

# Create a Quantum Circuit
qc = QuantumCircuit(num_qubits)

# Apply Hadamard gates to all qubits to create an equal superposition
qc.h(range(num_qubits))

# Phase Oracle: Flip the phase of the |101⟩ state
# Assuming the marked state is |101⟩
# To mark |101⟩, we need to flip the sign of |101⟩ state
qc.x(1)  # Flip qubit 1 to use a controlled-Z gate from qubit 0 and 2
qc.h(2)
qc.ccx(0, 1, 2)
qc.h(2)
qc.x(1)

# Diffuser (inversion about the mean)
# Apply Hadamard gates
qc.h(range(num_qubits))
# Apply X gates
qc.x(range(num_qubits))
# Apply a multi-controlled-Z gate (CCZ) using the same trick
qc.h(2)
qc.ccx(0, 1, 2)
qc.h(2)
# Apply X gates
qc.x(range(num_qubits))
# Apply Hadamard gates
qc.h(range(num_qubits))