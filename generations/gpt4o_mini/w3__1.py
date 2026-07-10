from qiskit import QuantumCircuit

qc = QuantumCircuit(3)

# Create the W state |001> + |010> + |100>
qc.x(0)  # Apply X gate to the first qubit to get |100>
qc.h(1)  # Apply H gate to the second qubit
qc.cx(1, 2)  # Apply CNOT gate from second qubit to third qubit
qc.h(0)  # Apply H gate to the first qubit
qc.cx(0, 1)  # Apply CNOT gate from first qubit to second qubit