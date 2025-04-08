import openai
from openai import OpenAI
import os

# 创建客户端实例（1.0+ 标准方式）
client = OpenAI(
    api_key=os.getenv("ONEAPI_API_KEY"),  # 从环境变量获取 API Key
    base_url="http://127.0.0.1:3000/v1"  # 替换为你的 one-api 地址
)

models_to_test = [
    "llama3.2:1b",
    "phi4:14b",
    "qwen2.5:14b",
    "qwen2.5:0.5b",
    "qwq:32b",
    "deepseek-r1:14b"

]
prompt = "你好，测试一下模型是否可用。"

for model in models_to_test:
    print(f"正在测试模型：{model}")
    try:
        # 使用 ChatCompletion 接口（新版标准）
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],  # 消息体格式变更
            temperature=0.5
        )
        print(f"模型 {model} 可用，返回结果：")
        print(response.choices[0].message.content)  # 响应数据结构变更
    except openai.APIError as e:  # 使用新版异常类型
        print(f"模型 {model} 测试出错：{e}")
    except Exception as e:
        print(f"其他异常：{e}")

    print("-" * 50)
