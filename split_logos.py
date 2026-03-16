# -*- coding: utf-8 -*-
from PIL import Image
import os

# 读取原始图片
input_path = r"C:\Users\Administrator\.openclaw\media\inbound\b283c5d0-ab47-4187-991d-d1d2bb1c9f94.jpg"
output_dir = r"C:\Users\Administrator\.openclaw-zero\workspace\logos"

# 创建输出目录
os.makedirs(output_dir, exist_ok=True)

# 打开图片
img = Image.open(input_path)
width, height = img.size

print(f"原始图片尺寸: {width} x {height}")

# 计算每个 LOGO 的尺寸（4x4 网格）
logo_width = width // 4
logo_height = height // 4

print(f"每个 LOGO 尺寸: {logo_width} x {logo_height}")

# LOGO 名称映射
logo_names = [
    ["01-魚", "02-鷺島", "03-石岩", "04-佐"],
    ["05-站着吃烤肉", "06-步菜", "07-綿久", "08-空谷"],
    ["09-まき本店", "10-岛设计", "11-美容室", "12-春光堂書店"],
    ["13-一禾堂", "14-SUKOSHIYA", "15-うえ田", "16-熱鮮魚"]
]

# 裁剪每个 LOGO
for row in range(4):
    for col in range(4):
        # 计算裁剪区域
        left = col * logo_width
        top = row * logo_height
        right = left + logo_width
        bottom = top + logo_height
        
        # 裁剪
        logo = img.crop((left, top, right, bottom))
        
        # 保存
        name = logo_names[row][col]
        output_path = os.path.join(output_dir, f"{name}.png")
        logo.save(output_path, "PNG")
        
        print(f"✓ 已保存: {name}.png")

print(f"\n完成！共裁剪 {4*4} 个 LOGO")
print(f"保存位置: {output_dir}")
