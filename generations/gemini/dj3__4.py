from qiskit.circuit import QuantumCircuit

# Create a QuantumCircuit object with 3 qubits
qc = QuantumCircuit(3)

# 1. Apply Hadamards to all qubits
qc.h(range(3))
qc.barrier()

# 2. Implement the phase oracle for f(x) = x_0 XOR x_1
# This applies a phase of -1 if x_0 != x_1.
# This construction CNOT(c,t); Z(t); CNOT(c,t) applies a phase
# to the states |01> and |10> of the control and target qubits.
qc.cnot(0, 1)
qc.z(1)
qc.cnot(0, 1)
qc.barrier()

# 3. Apply Hadamards to all qubits again
qc.h(range(3))