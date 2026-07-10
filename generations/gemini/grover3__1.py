from qiskit.circuit import QuantumCircuit

# Initialize a 3-qubit quantum circuit
qc = QuantumCircuit(3)

# 1. Apply initial Hadamard gates to all qubits to create a uniform superposition
qc.h([0, 1, 2])

# --- Start of one full Grover iteration ---

# 2. Implement the phase oracle for the marked state |101>
# The oracle applies a phase of -1 to |101> and does nothing to other states.
# This is achieved by framing a multi-controlled Z gate with X-gates on the
# qubit(s) that are in the |0> state for the marked item.
# For |101>, qubit 1 is in the |0> state.
qc.x(1)

# Apply a doubly-controlled Z gate (CCZ), which flips the phase of |111>.
# Because of the surrounding X-gates, this effectively flips the phase of |101>.
qc.ccz(0, 1, 2)

# Uncompute the X-gate on qubit 1.
qc.x(1)

# 3. Implement the diffuser (reflection about the average amplitude)
# This is constructed as: H-X-CCZ-X-H on all qubits.

# Apply Hadamard gates to all qubits
qc.h([0, 1, 2])
# Apply X-gates to all qubits
qc.x([0, 1, 2])

# Apply a CCZ gate (this marks the |000> state in this basis)
qc.ccz(0, 1, 2)

# Apply X-gates to all qubits
qc.x([0, 1, 2])
# Apply Hadamard gates to all qubits
qc.h([0, 1, 2])

# --- End of one full Grover iteration ---