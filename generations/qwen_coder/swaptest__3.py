```python
from qiskit import QuantumCircuit

qc = QuantumCircuit(3)
qc.h(0)  # Apply H to the ancilla (qubit)
qc.x(1)  # Prepare qubit