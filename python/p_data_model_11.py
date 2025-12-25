# Python 数据模型

print('自定义类创建')
from typing import Any, Optional

class Object:
    def __new__(cls, *args, **kwargs) -> 'self':
        return object.__new__(cls)
    def __init__(self, *args, **kwargs):
        pass
    def __call__(self, *args, **kwargs) -> Any:
        pass
obj = Object()
print(obj)
print(obj())


print('上下文管理器')
class Object:
    # with 语句会将返回值绑定到 as 子句中的变量，如果有的话。
    def __enter__(self) -> Optional[Any]:
        print('__enter__')
        return [1, 2, 3]
    def __exit__(self, exc_type, exc_value, traceback):
        print('__exit__')
        pass

# 进入 with 之前调用 obj.__enter__() 并得到 alias（如果有返回的话）
with Object() as alias:
    for item in alias:
        print(item)
# 离开 with 后调用 obj.__exit__() ，不管是正常结束还是因异常抛出而离开。

obj = Object()
with obj as alias:
    for item in alias:
        print(item)
    pass
