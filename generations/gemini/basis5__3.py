from qiskit.circuit import QuantumCircuit

# Create a quantum circuit with 5 qubits
qc = QuantumCircuit(5)

# The state is |11010> (reading from qubit 4 to 0)
# Qubits start in the |0> state by default.
# Apply an X gate to flip a qubit from |0> to |1>.
qc.x(1)
qc.x(2)
qc.x(4)