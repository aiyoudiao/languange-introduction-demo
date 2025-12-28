# 通义千问 Qwen-Turbo 调用示例

import requests
import json

# 配置API密钥和请求URL
API_KEY = "your_api_key_here"  # 替换为你的API密钥
API_URL = "https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation"

# 定义请求头
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# 定义请求体
def create_request(prompt):
    return {
        "model": "qwen-turbo",
        "input": {
            "messages": [
                {
                    "role": "system",
                    "content": "你是一个乐于助人的AI助手。"
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        },
        "parameters": {
            "temperature": 0.7,
            "top_p": 0.95,
            "max_tokens": 1024
        }
    }

# 发送请求并获取响应
def get_response(prompt):
    try:
        # 创建请求数据
        request_data = create_request(prompt)
        
        # 发送POST请求
        response = requests.post(
            url=API_URL,
            headers=headers,
            data=json.dumps(request_data),
            timeout=30
        )
        
        # 检查响应状态码
        if response.status_code == 200:
            # 解析响应数据
            result = response.json()
            # 提取生成的内容
            if "output" in result and "text" in result["output"]:
                return result["output"]["text"]
            else:
                return f"响应格式错误: {result}"
        else:
            return f"请求失败，状态码: {response.status_code}, 响应: {response.text}"
    except Exception as e:
        return f"请求异常: {str(e)}"

# 示例用法
if __name__ == "__main__":
    # 示例1: 简单问答
    print("示例1: 简单问答")
    prompt1 = "什么是Python？"
    response1 = get_response(prompt1)
    print(f"问题: {prompt1}")
    print(f"回答: {response1}")
    print("=" * 50)
    
    # 示例2: 代码生成
    print("示例2: 代码生成")
    prompt2 = "写一个Python函数来计算斐波那契数列"
    response2 = get_response(prompt2)
    print(f"请求: {prompt2}")
    print(f"生成的代码: {response2}")
    print("=" * 50)
    
    # 示例3: 文本生成
    print("示例3: 文本生成")
    prompt3 = "写一首关于春天的短诗"
    response3 = get_response(prompt3)
    print(f"请求: {prompt3}")
    print(f"生成的诗歌: {response3}")
