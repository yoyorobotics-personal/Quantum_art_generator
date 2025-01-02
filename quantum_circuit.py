#yoyorobotics 2025/1/2
#quantum art first test quantum circuit
from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit import transpile
# 创建一个2量子比特的量子电路，并添加测量
qc = QuantumCircuit(2, 2)
qc.h(0)  # 对第一个量子比特应用Hadamard门
qc.cx(0, 1)  # 对第一个量子比特和第二个量子比特应用CNOT门
qc.measure([0,1], [0,1])  # 测量两个量子比特

# 使用Aer模拟器
backend = Aer.get_backend('qasm_simulator')
#job = execute(qc, backend, shots=1000)
new_circuit = transpile(qc, backend)
job = backend.run(new_circuit)
result = job.result()
counts = result.get_counts()

print("测量结果:", counts)
