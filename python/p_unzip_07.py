# 解构（解包）

print('解包:')
ip, port = '192.168.1.1', 8080
print(ip, port)
ip, port = ('192.168.1.1', 8080)
print(ip, port)
ip, port = ['192.168.1.1', 8080]
print(ip, port)

# 以下两种不行
# ip, port = {'192.168.1.1', 8080}
# print(ip, port)
# ip, port = { 'ip': '192.168.1.1', 'port': 8080 }
# print(ip, port)

print("适量解包")
ip,_,port = "192.168.1.1:8080".rpartition(':')
print(_)
print(ip, port)

print('过量解包')
major, minor, *rest = "1.10.1.beta".split('.') # *rest 获取剩余的元素，rest 只是变量名
print(major, minor)
print(rest)

print('解包取左边')
major, minor, *_ = "1.10.1.beta".split('.')
print(major, minor)

print('解包取右边')
*_, micro, level = "1.10.1.beta".split('.')
print(micro, level)

print('解包取两边')
major, *_, level = "1.10.1.beta".split('.')
print(major, level)

print('解包集合')
a, b, *_ = { 3, 2, 1} # 集合是无序的且不重复的，所以解包结果是乱序的
print(a, b, _)

print('解包迭代器')
a, b, *_ = range(10)
print(a, b, _)

print('解包字典')
a,b,*_ = dict(a=1, b=2, c=3)
print(a, b, _)
a,b,*_ = {'a':1, 'b':2, 'c':3}
print(a, b, _)
a,b,*_ = dict(a=1, b=2, c=3).values()
print(a, b, _)
a,b,*_ = {'a':1, 'b':2, 'c':3}.values()
print(a, b, _)

print('生成式中的解包')
chars = (*'hello world', *'python', *'j', 's')
print(chars)

digits = [*range(10), *'abcdefg']
print(digits)

part = {'zs': 18, 'ls': 19}
summary = { 'ww': 20, **part}
print(summary)


print('迭代中的解包')
students = [
    ('zs', 18),
    ('ls', 19),
    ('ww', 20)
]
for name, age in students:
    print(name, age)

students = [
    (1, ('zs', 18)),
    (2, ('ls', 19)),
]
for id, (name, age) in students:
    print(id, name, age)

print('函数中的解包')
def version(major, minor, *parts):
    print(major, minor, parts)
version(1, 10, 1, 'beta') # 类似 major, minor, *parts = (1, 10, 1, 'beta')

def version():
    parts = "1.10.1.beta".split('.')
    return *parts, 'x86'
print(version())
*parts, arch = version()
print(parts, arch)
