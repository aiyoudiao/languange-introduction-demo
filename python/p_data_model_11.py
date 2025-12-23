# Python 数据模型

print('自定义类创建')
from typing import Any

class Object:
    def __new__(cls, *args, **kwargs) -> 'self':
        return object.__new__(cls)
    def __init__(self, *args, **kwargs):
