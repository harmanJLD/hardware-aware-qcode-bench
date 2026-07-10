from qiskit import QuantumCircuit

# Initialize a 3-qubit quantum circuit
qc = QuantumCircuit(3)

# 1. Initial Hadamards to create superposition
# This puts the register in the state |+>|+>|+>
qc.h(range(3))
qc.barrier()

# 2. Phase Oracle for the marked state |101>
# In Qiskit's little-endian ordering, |q2 q1 q0>, this is q0=1, q1=0, q2=1.
# Apply X-gate to the qubit that is 0 in the marked state.
qc.x(1)

# Apply a multi-controlled Z-gate (CCZ) to flip the phase of the target state.
# A CCZ gate can be constructed from a CCX (Toffoli) gate surrounded by Hadamards
# on the target qubit.
qc.h(2)
qc.ccx(0, 1, 2)
qc.h(2)

# Uncompute the X-gate to restore the original state basis.
qc.x(1)
qc.barrier()

# 3. Diffuser (inversion about the mean)
# The diffuser can be seen as an oracle for the |000> state, surrounded by Hadamards.
qc.h(range(3))
qc.x(range(3))

# Apply CCZ gate
qc.h(2)
qc.ccx(0, 1, 2)
qc.h(2)

qc.x(range(3))
qc.h(range(3))