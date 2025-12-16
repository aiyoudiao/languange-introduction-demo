
# 控制台打印
print('Hello，world!')

# 变量
age = 18
name = "张三"
print(name, 'age:', age)

# 字符串切片
msg = "Hello, world!"
print(msg[2:5])

# 列表
my_list = []
my_list.append(1)
my_list.append(2)
print('列表内容:')
for item in my_list:
    print(item)

# 判断
num = 200
print('判断:')
if num > 100:
    print('num > 100')
else:
    print('num <= 100')

# 循环
print('循环:')
for item in range(6):
    if item == 3: break
    print(item)
else:
    print('循环结束')

# 函数
def my_func():
    print('my_func: hi')
my_func()

# 文件处理
print('文件处理:')
with open('./python/file/my_file.txt', 'r', encoding='utf8') as file:
    for line in file:
        print(line)

# 算术
print('算术:')
result = 10 + 20
print('10 + 20 =', result)
result = 40 - 20
print('40 - 20 =', result)
result = 10 * 20
print('10 * 20 =', result)
result = 40 / 20
print('40 / 20 =', result)
result = 40 // 20
print('40 // 20 =', result)
result = 41 % 20
print('41 % 20 =', result)
result = 10 ** 2
print('10 ** 2 =', result)

# 加等于
print('加等于:')
counter = 0
print(counter)
counter += 3
print(counter)
counter = 0
print(counter)
counter = counter + 3
print(counter)
message = 'Hello'
print(message)
message += ' world'
print(message)

# f-字符串 (Python 3.6+)
website = 'Quick Reference'
print(f"Hello, {website}")
num = 10
print(f"{num} + 20 = {num + 20}")
