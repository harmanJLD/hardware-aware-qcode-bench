from qiskit.circuit import QuantumCircuit

# Initialize a 3-qubit quantum circuit
qc = QuantumCircuit(3)

# 1. Initial Hadamards (create superposition)
qc.h([0, 1, 2])
qc.barrier()

# 2. Phase Oracle for marked state |101>
# The marked state has qubit 0=1, qubit 1=0, qubit 2=1.
# We apply a Z-gate controlled by q0=1, q1=0, and q2=1.
# This is equivalent to a CCZ gate where the control on qubit 1 is inverted.
# We achieve this by wrapping qubit 1 with X gates.
qc.x(1)
qc.ccz(0, 2, 1)  # ccz with controls on q0, q2 and target on q1
qc.x(1)
qc.barrier()

# 3. Diffuser (inversion about the mean)
# Apply Hadamards to all qubits
qc.h([0, 1, 2])
# Apply oracle for the |000> state
qc.x([0, 1, 2])
qc.ccz(0, 1, 2)
qc.x([0, 1, 2])
# Apply Hadamards to all qubits
qc.h([0, 1, 2])