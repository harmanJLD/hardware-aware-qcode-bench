import numpy as np
from qiskit import QuantumCircuit
from qiskit.circuit.library import QFT

# Initialize a quantum circuit with 3 counting qubits and 1 target qubit
# Qubits 0-2 are counting qubits (q0=LSB), qubit 3 is the target
qc = QuantumCircuit(4)

# 1. Prepare the eigenstate |1> on the target qubit (qubit 3)
# The T gate has eigenstate |1> with eigenvalue exp(i*pi/4)
qc.x(3)

# 2. Apply Hadamard transform to the counting qubits to create superposition
for qubit in range(3):
    qc.h(qubit)

# 3. Apply the controlled unitary operations (powers of controlled-T)
# The T gate is P(pi/4). Controlled powers of T are implemented with
# repeated applications of the controlled-phase gate.
repetitions = 1
for counting_qubit in range(3):
    for _ in range(repetitions):
        qc.cp(np.pi / 4, counting_qubit, 3)
    repetitions *= 2

# 4. Apply the inverse Quantum Fourier Transform on the counting register
# The Qiskit QFT object applies the transform assuming the first qubit in the
# list is the most significant. Since our MSB is qubit 2 and LSB is qubit 0,
# we pass the qubits in the order [2, 1, 0].
# The default `do_swaps=True` includes the required final SWAP gates.
iqft = QFT(num_qubits=3, inverse=True, name="IQFT")
qc.append(iqft, [2, 1, 0])