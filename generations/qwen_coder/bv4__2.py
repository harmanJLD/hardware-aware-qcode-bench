```python
from qiskit import QuantumCircuit

qc = QuantumCircuit(4)

# Apply Hadamards to all qubits
qc.h(range(4))

# Apply the phase oracle for the secret string s = 1101
# The phase oracle flips the sign of the state if the dot product of the input and s is