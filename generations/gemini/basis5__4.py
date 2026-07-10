from qiskit import QuantumCircuit

# Create a quantum circuit with 5 qubits
qc = QuantumCircuit(5)

# Apply X gates to flip the state of qubits 1, 2, and 4 from |0> to |1>
# Qubits are indexed from 0.
# The desired state is |q4 q3 q2 q1 q0> = |10110>
# Qubit 0: |0> (no gate needed)
# Qubit 1: |1> (apply X gate)
# Qubit 2: |1> (apply X gate)
# Qubit 3: |0> (no gate needed)
# Qubit 4: |1> (apply X gate)
qc.x(1)
qc.x(2)
qc.x(4)