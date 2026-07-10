from qiskit import QuantumCircuit

# Define the quantum circuit
qc = QuantumCircuit(4)

# Apply Hadamard gates to all qubits
qc.h(range(4))

# Apply the phase oracle for the secret string s = "1101"
qc.cz(0, 3)  # s_0=1 affects qubit 0 with qubit 3
qc.cz(1, 3)  # s_1=1 affects qubit 1 with qubit 3
# s_2=0 does not affect the oracle
qc.cz(3, 3)  # s_3=1 affects qubit 3 with itself (Z-gate)

# Apply Hadamard gates to all qubits again
qc.h(range(4))