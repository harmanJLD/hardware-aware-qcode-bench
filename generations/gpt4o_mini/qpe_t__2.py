from qiskit import QuantumCircuit

# Create a QuantumCircuit with 4 qubits (3 for counting, 1 for the eigenstate)
qc = QuantumCircuit(4)

# Prepare the eigenstate |1> on qubit 3
qc.x(3)

# Apply Hadamard gates to the counting qubits (0, 1, 2)
qc.h(0)
qc.h(1)
qc.h(2)

# Apply controlled powers of T gate
qc.cp(2 * np.pi / 4, 0, 3)  # Controlled T^1 on qubit 0
qc.cp(2 * np.pi / 2, 1, 3)  # Controlled T^2 on qubit 1
qc.cp(2 * np.pi, 2, 3)      # Controlled T^4 on qubit 2

# Inverse Quantum Fourier Transform (QFT)
qc.swap(0, 2)  # Swap the first and last qubits
qc.h(0)
qc.cp(-np.pi / 2, 1, 0)
qc.h(1)
qc.cp(-np.pi / 4, 2, 0)
qc.cp(-np.pi / 2, 2, 1)
qc.h(2)