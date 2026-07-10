from qiskit import QuantumCircuit
from qiskit.circuit.library import ZGate, HGate, XGate

# Number of qubits
n = 3

# Create a quantum circuit with n qubits
qc = QuantumCircuit(n)

# Apply Hadamard gates to all qubits to create superposition
qc.h(range(n))

# Define the phase oracle for the marked state |101>
qc.x(1)  # Flip qubit 1 (|0> -> |1>) to match |101>
qc.cz(0, 2)  # Apply controlled-Z where qubit 0 is control and qubit 2 is target
qc.x(1)  # Flip qubit 1 back (|1> -> |0>) to original state

# Apply the diffuser (inversion about the mean)

# Apply Hadamard gates to all qubits
qc.h(range(n))

# Apply X gates to all qubits
qc.x(range(n))

# Apply multi-controlled Z gate (equivalent to applying controlled-Z with all qubits as control)
qc.h(n-1)
qc.mcx(list(range(n-1)), n-1)  # Multi-controlled X gate with last qubit as target
qc.h(n-1)

# Apply X gates to all qubits
qc.x(range(n))

# Apply Hadamard gates to all qubits
qc.h(range(n))