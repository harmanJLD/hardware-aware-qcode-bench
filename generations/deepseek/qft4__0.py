from qiskit import QuantumCircuit

# Create a QuantumCircuit object with 4 qubits
qc = QuantumCircuit(4)

# Apply the Quantum Fourier Transform
for qubit in range(2):
    qc.h(qubit)
    for control_qubit in range(qubit + 1, 4):
        theta = 2 * (3.141592653589793) / (2 ** (control_qubit - qubit + 1))
        qc.cp(theta, control_qubit, qubit)

# Apply the final qubit-reversal SWAP gates
qc.swap(0, 3)
qc.swap(1, 2)