from qiskit import QuantumCircuit

# Create a QuantumCircuit with 8 qubits
qc = QuantumCircuit(8)

# Put the first qubit in a superposition state |+>
qc.h(0)

# Entangle the other qubits using a chain of CNOT gates
for i in range(1, 8):
    qc.cx(0, i)