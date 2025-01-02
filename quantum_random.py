#yoyorobotics 2025/1/2
#quantum art first test quantum random number

from qiskit import QuantumCircuit
from qiskit import transpile
import numpy as np
from qiskit_aer import Aer
def generate_quantum_random_bits(n_qubits):
    """
    生成n_qubits个量子随机比特
    """
    qc = QuantumCircuit(n_qubits, n_qubits)
    qc.h(range(n_qubits))  # 将量子比特初始化到叠加态
    qc.measure(range(n_qubits), range(n_qubits))  # 测量量子比特
    backend = Aer.get_backend('qasm_simulator')
    #job = execute(qc, backend, shots=1)
    new_circuit = transpile(qc, backend)
    job = backend.run(new_circuit)
    result = job.result()
    counts = result.get_counts()
    bitstring = list(counts.keys())[0]
    return bitstring

# 示例：生成8个量子随机比特
random_bits = generate_quantum_random_bits(8)
print(f"量子随机比特：{random_bits}")
