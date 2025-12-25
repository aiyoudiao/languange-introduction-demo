# Python 类型标注 (Python 3.5+)
print('类型标注：')

print('变量')
string: str = "halo world "
times: int = 3
print(string * times)

result: str = 1 + 2
print(result)

print('参数')
def say_hi(name: str, start: str = 'hi'):
    return start + ', ' + name
print(say_hi('张三'))

print('位置参数')
def calc_sum(*args: int):
    return sum(args)
print(calc_sum(*[1, 2, 3, 4, 5]))

print('返回值')
def say_hi2(name) -> str:
    return 'hello, ' + name
print(say_hi2('张三'))


print('多种可能的返回值')
from typing import Union
def respond(status) -> Union[str, int]:
    return "Ok" if status else 200
print(respond(False))

print('关键字参数')
def calc_sum(**kwargs: int):
    return sum(kwargs.values())
print(calc_sum(a=1, b=2, c=3))

print('多个返回值')
def respond() -> (int,str):
    return 200, "Ok"
print(respond())

print('多种可能的返回值')
def respond(status) -> int|str:
    return "Ok" if status else 200
print(respond(False))

print('属性')
class Person:
    name: str = 'zs'
    age: int = 18
    
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.graduated: bool = False
p = Person('zs', 18)
print(p.name, p.age, p.graduated)

print('标注自己')
class Person:
    name: str
    age: int
    
    def set_name(self, name) -> "Person":
        self.name = name
        return self
p = Person()
p.set_name('zs').age = 18
print(p.name, p.age)

print('标注自己 3.11+')
from typing import Self

class Person:
    name: str
    age: int
    
    def set_name(self: Self, name) -> Self:
        self.name = name
        return self

p = Person()
p.set_name('zs').age = 18
print(p.name, p.age)

print('标注一个值为类型的参数')
from typing import TypeVar, Type
T = TypeVar('T')

def converter(raw, mapper: Type[T], default: T) -> T:
    try:
        return mapper(raw)
    except:
        return default

# raw: str = input('请输入数字：')
# result: int = converter(raw, mapper=int, default=0)
# print(result)

print('标注一个值为函数的参数')
from typing import TypeVar, Callable, Any

T = TypeVar("T")

def converter(raw, mapper: Callable[[Any], T], default: T) -> T:
    try:
        return mapper(raw)
    except:
        return default

def is_success(value) -> bool:
    return value in (0, "Ok", True, 'success')

resp = dict(code = 0, message = "Ok", data = [])
success: bool = converter(resp['message'], mapper=is_success, default= False)
print(success)
