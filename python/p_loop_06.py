# 循环

print('for 循环')
li = [2, 3, 5, 7]
for item in li:
    print(item)

print('for 循环带索引')
li = ['apple', 'banana', 'orange']
for index, item in enumerate(li):
    print(f"{index} {item}")

print("while 循环")
i = 0
while i < 5:
    print(i)
    i += 1

print("结束循环与跳过一轮循环")
i = 0
for index in range(10):
    i = index * 10
    if index == 5:
        break
    if index % 2 == 0:
        continue
    print(f'{index} -> {i}')

print("范围循环")
for i in range(5): # 0 到 4 [0,5)
    print(i)
print('---')

for i in range(4, 10):
    print(i)
print('---')

for i in range(4, 10, 2):
    print(i)


print("zip 遍历多个列表")
name = ['张三', '李四', '王五']
age = [18, 20, 25]
sex = ['男', '女', '男']

for n, s, a in zip(name, sex, age):
    print(f"姓名：{n} 性别：{s} 年龄：{a}岁")

print("列表推导式")
li = [x ** 2 for x in range(1, 11)] # 创建一个列表，通过 for 循环生成 1 到 10 的数字的平方
print(li)
