#yoyorobotics 2025/1/2
#quantum art first test art generator interactive

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import io
from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit import transpile
import matplotlib.pyplot as plt

def generate_quantum_random_bits(n_qubits=8):
    """
    生成n_qubits个量子随机比特
    """
    qc = QuantumCircuit(n_qubits, n_qubits)
    qc.h(range(n_qubits))  # 将所有量子比特置于叠加态
    qc.measure(range(n_qubits), range(n_qubits))  # 测量量子比特

    backend = Aer.get_backend('qasm_simulator')
    #job = execute(qc, backend, shots=1)
    new_circuit = transpile(qc, backend)
    job = backend.run(new_circuit)
    result = job.result()
    counts = result.get_counts()
    bitstring = list(counts.keys())[0]
    return bitstring

def bits_to_color(bits):
    """
    将8位比特转换为RGB颜色
    """
    red = int(bits[0:2], 2) * 85  # 00=0, 01=85, 10=170, 11=255
    green = int(bits[2:4], 2) * 85
    blue = int(bits[4:6], 2) * 85
    return (red/255, green/255, blue/255)

def bits_to_shape(bits):
    """
    根据比特决定形状
    """
    shape_code = bits[6:8]
    if shape_code == '00':
        return 'circle'
    elif shape_code == '01':
        return 'square'
    elif shape_code == '10':
        return 'triangle'
    else:
        return 'star'

def generate_art(bits, size=100):
    """
    生成艺术图案并返回图像对象
    """
    color = bits_to_color(bits)
    shape = bits_to_shape(bits)

    fig, ax = plt.subplots(figsize=(4,4))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_facecolor('black')

    if shape == 'circle':
        circle = plt.Circle((5, 5), 3, color=color, fill=True)
        ax.add_patch(circle)
    elif shape == 'square':
        square = plt.Rectangle((2, 2), 6, 6, color=color, fill=True)
        ax.add_patch(square)
    elif shape == 'triangle':
        triangle = plt.Polygon([[5, 8], [2, 2], [8, 2]], color=color)
        ax.add_patch(triangle)
    elif shape == 'star':
        star = plt.Polygon([[5, 9], [6, 7], [8, 7], [6.5, 5], [7.5, 3], [5, 4.5],
                            [2.5, 3], [3.5, 5], [2, 7], [4, 7]], color=color)
        ax.add_patch(star)

    plt.axis('off')

    # 将Matplotlib图像保存到字节流
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img = Image.open(buf)
    plt.close(fig)
    return img

def generate_and_display_art():
    bits = generate_quantum_random_bits(8)
    img = generate_art(bits)
    img = ImageTk.PhotoImage(img)

    # 更新图像标签
    art_label.config(image=img)
    art_label.image = img  # 保持引用

    # 更新比特标签
    bits_label.config(text=f"量子随机比特：{bits}")

# 创建主窗口
root = tk.Tk()
root.title("量子艺术生成器")
root.geometry("500x600")
root.configure(bg='white')

# 创建生成按钮
generate_button = ttk.Button(root, text="生成艺术", command=generate_and_display_art)
generate_button.pack(pady=20)

# 创建比特显示标签
bits_label = ttk.Label(root, text="量子随机比特：", font=("Arial", 12), background='white')
bits_label.pack(pady=10)

# 创建图像展示标签
art_label = ttk.Label(root, background='white')
art_label.pack(pady=10)

from tkinter import filedialog

def save_art():
    bits = bits_label.cget("text").split("：")[1]
    img = generate_art(bits)
    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
    if file_path:
        img.save(file_path)
        print(f"艺术作品已保存至 {file_path}")

# 添加保存按钮
save_button = ttk.Button(root, text="保存艺术", command=save_art)
save_button.pack(pady=10)

# 运行主循环
root.mainloop()
