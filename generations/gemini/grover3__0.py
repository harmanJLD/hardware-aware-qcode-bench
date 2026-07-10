from qiskit import QuantumCircuit

# Initialize a 3-qubit quantum circuit
qc = QuantumCircuit(3)

# 1. Initial Hadamards: Create uniform superposition
qc.h([0, 1, 2])
qc.barrier()

# 2. Phase Oracle for marked state |101>
# The marked state has qubit 0=1, qubit 1=0, qubit 2=1.
# To mark a state |s>, we apply X gates on qubits i where s_i=0,
# then a multi-controlled Z gate, then uncompute the X gates.
# For |101>, the bitstring is 101 (q2=1, q1=0, q0=1). We apply an X-gate to qubit 1.
qc.x(1)
# Apply a multi-controlled Z-gate (CCZ). This flips the phase of the |111> state.
# A CCZ can be implemented using mcz with 2 controls and 1 target.
qc.mcz([0, 2], 1)
# Uncompute the X-gate.
qc.x(1)
qc.barrier()

# 3. Diffuser (Amplitude Amplification)
# This operator reflects the states about the average amplitude.
# It can be constructed as H_n @ (2|0><0| - I) @ H_n
# Apply Hadamards to all qubits
qc.h([0, 1, 2])
# Implement the (2|0><0| - I) operator, which flips the phase of |000>
qc.x([0, 1, 2])
qc.mcz([0, 1], 2)
qc.x([0, 1, 2])
# Apply Hadamards to all qubits
qc.h([0, 1, 2])