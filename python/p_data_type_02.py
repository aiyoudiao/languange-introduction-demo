# python 数据类型

# 字符串
print('字符串:')
hello = 'hello world'
print(hello)
hello = "hello world"
print(hello)
multi_line = """
hello world
 hello world
  hello world
"""
print(multi_line)

# 数值
print('数值:')
x = 1
y = 1.1
z = 1j
print(x, y, z)
print(type(x), type(y), type(z))

# 布尔值
print('布尔值:')
a = True
b = False
print(a, b)
print(type(a), type(b))
print(bool(0), bool(1))

# 列表
print('列表:')
list1 = [1, 2, 3]
print(list1)
list2 = ['hello', 'world', '!']
print(list2)
list3 = [True, False, True]
print(list3)
list4 = list((1, 5, 7, 9, 3))
print(list4)
print(type(list4))

# 元组 类似列表，但自身不可变
print('元组:')
my_tuple = (1, 2, 3)
print(my_tuple)
my_tuple = tuple((1, 5, 7, 9, 3))
print(my_tuple)
print(type(my_tuple))

# 集合 类似列表，但里面的元素是无序而不重复的
print('集合:')
set1 = {'a', 'b', 'c'}
set2 = set(('a', 'b', 'c'))
print(set1, set2)
print(type(set1), type(set2))

# 字典 键-值对，一种像 JSON 那样对象
print('字典:')
empty_dict = {}
a = {"one": 1, "two": 2, "three": 3}
print(empty_dict, a)
print(type(empty_dict), type(a))
print('a[\'one\']', a['one'])
print('a.keys()', a.keys())
print('a.values()', a.values())
a.update({'four': 4})
print('a.keys()', a.keys())
print('a[\'four\']', a['four'])

# 类型转换
print('类型转换:')

print('转换为整数')
print('int(1) ', int(1))
print('int(2.8) ', int(2.8))
print(f"int('3') {int('3')}")

print('转换为浮点数')
print(f"float(1) {float(1)}")
print(f"float(2.8) {float(2.8)}")
print(f"float('3') {float('3')}")
print(f"float('4.2') {float("4.2")}")

print("转换为字符串")
print(f"str('s1') {str('s1')}")
print(f"str(2) {str(2)}")
print(f"str(3.0) {str(3.0)}")

