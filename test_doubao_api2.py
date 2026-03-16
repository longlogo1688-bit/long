import requests
import json

# 测试新 token
token = "K6Zdl3VLUmpIeO4zamrLHLqJe3ViYxfcsjZ-V_xVnT_jksLixl3UOpE2zZmqBr33UN1SRrBnqDwlNeOIykKO_9a35jAPWtWm8aqke2Rl7Qb1rUe4H87aOGrhahw9DEGqHcGZNZ3F65Cd-k7xizITOXeBD1LGArmPdd0FsrbK"

# 1. 测试 token check 接口
print("=== 测试 Token 有效性 ===")
try:
    response = requests.post(
        "http://localhost:8000/token/check",
        headers={"Content-Type": "application/json"},
        json={"token": token},
        timeout=10
    )
    print(f"Token Check 响应: {response.json()}")
except Exception as e:
    print(f"Token Check 失败: {e}")

# 2. 测试对话接口
print("\n=== 测试对话接口 ===")
try:
    response = requests.post(
        "http://localhost:8000/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        },
        json={
            "model": "doubao",
            "messages": [{"role": "user", "content": "你好，请简单介绍一下自己"}],
            "stream": False
        },
        timeout=30
    )
    result = response.json()
    print(f"状态码: {response.status_code}")
    if "choices" in result:
        print(f"回复: {result['choices'][0]['message']['content']}")
    else:
        print(f"响应: {json.dumps(result, indent=2, ensure_ascii=False)}")
except Exception as e:
    print(f"对话测试失败: {e}")
