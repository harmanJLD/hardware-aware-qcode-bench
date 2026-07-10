from qiskit import QuantumCircuit

# Create an 8-qubit quantum circuit
num_qubits = 8
qc = QuantumCircuit(num_qubits)

# Put the first qubit in a superposition state
qc.h(0)

# Create entanglement using a cascade of CNOT gates
for i in range(num_qubits - 1):
    qc.cx(i, i + 1)