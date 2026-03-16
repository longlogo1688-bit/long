# -*- coding: utf-8 -*-
import requests
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

token = "41dd094e32a97bc496140f7dfe10f2c8"

print("=== 生成 B字母+小狗 LOGO ===\n")

try:
    response = requests.post(
        "http://localhost:8000/v1/images/generations",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        },
        json={
            "model": "Seedream 4.0",
            "prompt": "一个现代简约风格的LOGO设计，字母B的形状与可爱的小狗形象巧妙结合，B的下半部分形成小狗的头部轮廓，整体线条流畅，适合作为品牌标识，白色背景，矢量风格，专业设计",
            "ratio": "1:1",
            "style": "简约",
            "stream": False
        },
        timeout=60
    )
    result = response.json()
    
    print(f"状态码: {response.status_code}")
    print(f"\n完整响应:\n{json.dumps(result, indent=2, ensure_ascii=False)}\n")
    
    # 提取图片URL
    if "choices" in result and len(result["choices"]) > 0:
        message = result["choices"][0]["message"]
        if "images" in message:
            images = message["images"]
            print(f"生成的图片链接:")
            for i, img_url in enumerate(images, 1):
                print(f"  图片{i}: {img_url}")
        else:
            print(f"回复内容: {message.get('content', '无内容')}")
    else:
        print(f"响应: {result}")
        
except Exception as e:
    print(f"生成失败: {e}")
    import traceback
    traceback.print_exc()
