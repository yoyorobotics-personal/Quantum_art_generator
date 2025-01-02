#yoyorobotics 2025/1/2
#quantum art first test art shape

import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import io
from quantum_random import*

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
    生成艺术图案
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
    plt.show()

# 测试艺术生成
generate_art(random_bits)
