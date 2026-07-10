from qiskit import QuantumCircuit

# Create a QuantumCircuit with 3 qubits
qc = QuantumCircuit(3)

# Apply Hadamard gates to all qubits
qc.h(0)
qc.h(1)
qc.h(2)

# Define the phase oracle for the balanced function f(x) = x_0 XOR x_1
qc.cz(0, 1)  # This applies a controlled-Z gate, which introduces a phase of -1 when both qubits are |1>

# Apply Hadamard gates to all qubits again
qc.h(0)
qc.h(1)
qc.h(2)