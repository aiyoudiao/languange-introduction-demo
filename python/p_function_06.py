# 函数

print('函数定义：')
def hello_world():
    print('hello world')

hello_world()

print("函数返回值")
def add(x, y):
    print(f'{x} + {y} = {x + y}')
    return x + y
print(add(1, 2))

print("函数参数(将「参数玩法」做成语言级特性)")
def varargs(*args): # *args 表示：接收任意数量的位置参数，会将参数打包成一个元组
    return args
print(varargs(1, 2, 3))
def keywords_args(**kwargs): # **kwargs ：接收任意数量关键字参数，会将参数打包成一个字典
    return kwargs
print(keywords_args(a=1, b=2, c=3))
def varargs_and_keywords_args(first, *args, **kwargs): # 正常参数，*args, **kwargs 组合形式
    print(first)
    print(args)
    print(kwargs)
# 记住函数参数的变量名不能有传入进来的键名，比如 第一个参数为 first，那么传入的 kwargs 中不能存在 first 这个键
# 不然会报错 TypeError: varargs_and_keywords_args() got multiple values for argument 'first'
varargs_and_keywords_args(1, 2, 3, a=1, b=2, c=3)


print("返回多个参数")
def swap(a, b):
    return b, a
a, b = swap(1, 2)
print(a, b)

print("默认值")
def add(x, y=1):
    return x + y
print(add(1))
print(add(1, 2))

print("匿名函数 lambda")
add = lambda x, y: x + y
print(add(1, 2))
print((lambda x, y: x ** 2 + y ** 2)(1, 2))
