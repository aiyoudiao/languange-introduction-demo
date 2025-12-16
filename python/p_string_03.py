# python 字符串

print('下标访问：')
hello = 'hello world'
print(hello[0])
print(hello[-1])
print(type(hello[-1]))

print('循环：')
for item in "test":
    print(item)

print('获取长度：')
print(len("hello world"))

print("重复多次：")
print("===+"*8)

print('存在性判断：')
s = 'hello world'
print(f" s = '{s}'")
print(f" hello in s { 'hello' in s }")
print(f" test not in s { 'test' not in s }")

print('字符串拼接：')
s = 'hello'
t = 'world'
w = s + ' ' + t
print(w)
print('hello' ' ' 'world') # 两个字符串之间可以省略加号

print('字符串格式化：')
name = '张三'
print("你好，%s!" % name)
name = '李四'
age = 18
print("%s is %d years old." % (name, age))
