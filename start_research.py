#!/usr/bin/env python3
"""Start a deep research task on how to become a senior design master"""

import sys
import os
sys.path.append(r'C:\Users\Administrator\.openclaw-zero\workspace\deer-flow\backend\packages\harness')

from deerflow.client import DeerFlowClient

# Initialize client
client = DeerFlowClient()

# The research task
task = """深度研究：系统学习如何成为一个高级设计大师

请帮我整理：
1. 高级设计师和初级设计师的核心区别
2. 成为高级设计大师必须掌握的知识体系（分阶段）
3. 顶级设计师的思维方式和工作方法
4. 值得推荐的学习资源、经典书籍和案例
5. 练习和进阶的实践路径

请给出全面、结构化的深度研究报告。
"""

print("Starting research task...")
print("Task:", task)

# Start chat
response = client.chat(task, thread_id="design-master-research")
print("\nResponse received:")
print(response)
