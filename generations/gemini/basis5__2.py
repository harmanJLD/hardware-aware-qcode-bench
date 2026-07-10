from qiskit import QuantumCircuit

# Create a quantum circuit with 5 qubits
qc = QuantumCircuit(5)

# Apply X gates to qubits 1, 2, and 4 to flip them from |0> to |1>
# The desired state is |q4 q3 q2 q1 q0> = |10110>
qc.x(1)
qc.x(2)
qc.x(4)