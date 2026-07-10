from qiskit import QuantumCircuit

qc = QuantumCircuit(3)

# Prepare the W state (|001> + |010> + |100>)/sqrt(3)
qc.ry(2 * np.arccos(1 / np.sqrt(3)), 0)
qc.ch(0, 1)
qc.cx(1, 2)
qc.cx(0, 1)
qc.x(0)