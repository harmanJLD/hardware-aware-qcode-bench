```python
from qiskit import QuantumCircuit

qc = QuantumCircuit(3)

# Apply Hadamard gates to all qubits
qc.h([0, 1, 2])

# Phase oracle for the function f(x) = x_0 XOR x_