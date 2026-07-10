from qiskit import QuantumCircuit

# Create a quantum circuit with 3 qubits
qc = QuantumCircuit(3)

# 1. Initial Hadamards to create superposition
qc.h([0, 1, 2])

# 2. Phase Oracle for the marked state |101>
# The state |101> corresponds to q2=1, q1=0, q0=1.
# We want to apply a phase flip only to this state.
# A CCZ gate flips the phase of |111>. To mark |101>, we
# temporarily flip the state of qubit 1 before and after the CCZ.
qc.x(1)
qc.ccz(0, 1, 2)
qc.x(1)

# 3. Diffuser (inversion about the mean)
# Apply H to all qubits
qc.h([0, 1, 2])
# Apply an oracle for the state |000>
qc.x([0, 1, 2])
qc.ccz(0, 1, 2)
qc.x([0, 1, 2])
# Apply H to all qubits
qc.h([0, 1, 2])