from qiskit import QuantumCircuit

def qft_4_qubits():
    qc = QuantumCircuit(4)
    
    # Apply Hadamard gates and controlled rotations
    qc.h(0)
    qc.cp(1.5708, 0, 1)  # pi/2
    qc.cp(0.7854, 0, 2)  # pi/4
    qc.cp(0.3927, 0, 3)  # pi/8
    
    qc.h(1)
    qc.cp(1.5708, 1, 2)  # pi/2
    qc.cp(0.7854, 1, 3)  # pi/4
    
    qc.h(2)
    qc.cp(1.5708, 2, 3)  # pi/2
    
    qc.h(3)
    
    # Apply SWAP gates to reverse the qubit order
    qc.swap(0, 3)
    qc.swap(1, 2)
    
    return qc

qc = qft_4_qubits()