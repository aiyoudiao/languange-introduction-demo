## 通义千问 Qwen-Turbo 调用的示例

### 1. 简介
通义千问（Qwen-Turbo）是阿里云开发的大语言模型，本示例展示了如何使用Python调用Qwen-Turbo的API进行文本生成。

### 2. 准备工作

#### 2.1 获取API密钥
1. 登录阿里云控制台
2. 进入通义千问控制台
3. 创建API密钥并保存

#### 2.2 安装依赖
```bash
pip install requests
```

### 3. 代码示例

```python
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
```

### 4. 参数说明

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `temperature` | 控制生成文本的随机性，值越大越随机 | 0.7 |
| `top_p` | 控制核采样的概率阈值，值越大生成的文本越丰富 | 0.95 |
| `max_tokens` | 控制生成文本的最大长度 | 1024 |

### 5. 使用方法

1. 将代码保存为`qwen_turbo_demo.py`
2. 替换`API_KEY`为你的实际API密钥
3. 运行代码：
   ```bash
   python qwen_turbo_demo.py
   ```

### 6. 常见问题

#### 6.1 API密钥无效
请检查API密钥是否正确，以及是否具有调用Qwen-Turbo的权限。

#### 6.2 请求超时
如果网络不稳定，可能会导致请求超时，可以适当调整`timeout`参数。

#### 6.3 响应格式错误
API返回的格式可能会更新，请检查最新的API文档。

### 7. 进阶使用

#### 7.1 多轮对话
可以通过在`messages`中添加历史对话来实现多轮对话：

```python
def create_multi_turn_request(messages):
    return {
        "model": "qwen-turbo",
        "input": {
            "messages": messages
        },
        "parameters": {
            "temperature": 0.7,
            "top_p": 0.95,
            "max_tokens": 1024
        }
    }

# 使用示例
messages = [
    {"role": "system", "content": "你是一个数学老师。"},
    {"role": "user", "content": "什么是勾股定理？"},
    {"role": "assistant", "content": "勾股定理是指直角三角形的两条直角边的平方和等于斜边的平方。"},
    {"role": "user", "content": "如何证明勾股定理？"}
]
```

#### 7.2 自定义系统提示词
可以通过修改`system`角色的`content`来定义AI助手的行为：

```python
messages = [
    {"role": "system", "content": "你是一个专业的Python开发工程师，回答问题时请使用简洁明了的语言。"},
    {"role": "user", "content": "如何优化Python代码的性能？"}
]
```

### 8. 注意事项

1. 请保护好你的API密钥，不要在公开代码中泄露
2. 合理设置请求频率，避免超过API调用限制
3. 根据实际需求调整生成参数，以获得最佳效果
4. 处理好API调用可能出现的异常情况


