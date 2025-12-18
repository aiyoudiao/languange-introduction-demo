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

txt1 = "my name is {name}, I'm {age} years old.".format(name='张三', age=18)
print(txt1)
txt2 = "my name is {0}, I'm {1} years old.".format('张三', 18)
print(txt2)
txt3 = "my name is {}, I'm {} years old.".format('张三', 18)
print(txt3)

# print('控制台输入：')
# name = input('请输入你的名字：')
# print('hello,', name)

print('list 拼接字符串，插入分隔符')
names = ['张三', '李四', '王五']
print('、'.join(names))

print('字符串切割')
str = 'hello world'
print('[1,)' + str[1:2])
print('[0,5)', str[0:5])
print('[0,5)', str[:5])
print(str[6:])
print(str[:5] + str[5:])
print('全部 '+ str[:])
print(str[-5:-1])

str = '12345' * 10
print(str)
print('步长，每隔多少个字符取一个字符 [start:end:step] start 默认为0， end 默认为字符串长度， step 默认步长为 1')
print(str[::5])
print(str[0:len(str):5]) # 索引 0 5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95 100 各取一个字符
print(str[4::5]) # 索引 4 9 14 19 24 29 34 39 44 49 54 59 64 69 74 79 84 89 94 99 各取一个字符
print(str[::-5]) # 索引 100 95 90 85 80 75 70 65 60 55 50 45 40 35 30 25 20 15 10 5 0 各取一个字符
print(str[::-1]) # 索引 0 1 2 3 4 ... 99 100 各取一个字符 字符串会倒立

print('头尾判断')
print('hello python'.startswith('hello')) # 字符串开头判断
print('hello python'.startswith('H')) # 字符串开头判断
print('hell python'.endswith('python')) # 字符串末尾判断


print('3.6 新特性 f-字符串 模板字符串')
name = '张三'
print(f"hello, {name}")
num = 10
print(f'{num} + 20 = {num + 20}')
print(f"""hello, {"python"}""") # 可多行的模板字符串
print(f"hello, {"{name}"} ?")
print(f"{{5}} + {{10}} = {{5 + 10}}") # 占位符被转义了
print(f"""
      多行字符串:
      hello
      {name}
""")

print('字符串填充对齐')
print(f'{"text":10}')
print(f"{"text":*>10}") # 填充字符 *，> 表示向左填充
print(f"{"text":*<10}") # 填充字符 *，< 表示向右填充
print(f'{"text":*^10}') # 填充字符 *，^ 居中填充
print(f'{12345:0>10}') # 填充字符 0，> 向左填充 0，用数字来填充

print('显示正负号')
print(f'{12345:+}')
print(f'{-12345:+}')
print(f'{12345:+10}') # 填充字符 +，> 向左填充 空格
print(f'{12345:+010}') # 填充字符 +，> 向左填充 0
print(f'{-12345:+010}') # 显示负号 -，> 向左填充 0

print("按类型输出")
print(f'{10:b}') # 输出二进制
print(f'{10:o}') # 输出八进制
print(f'{10:x}') # 输出小写的十六进制
print(f'{10:X}') # 输出大写的十六进制
print(f'{100:e}') # 输出科学计数法
print(f'{10000:c}') # 输出对应的字符
print(f'{10:#b}') # 输出二进制，# 表示添加 0b 前缀
print(f'{10:#o}') # 输出八进制，# 添加 0o 前缀
print(f'{10:#x}') # 输出十六进制，# 添加 0x 前缀

print("其它")
print(f'{-12345:0=10}') # 填充字符 0，= 填充字符，> 向左填充 0
print(f'{12345:010}') # 填充字符 0，> 向左填充 0
print(f'{-12345:010}') # 填充字符 0，> 向左填充 0
import math
print(f'{math.pi}') # 输出浮点数
print(f'{math.pi:.2f}') # 保留两位小数
print(f'{10000:,.2f}') # 添加千分位分隔符，.2f 保留两位小数
print(f'{10000:_.2f}') # 添加千分位分隔符_.2f 保留两位小数
print(f'{0.25:0%}') # 输出百分比
print(f'{0.25:.0%}') # 输出百分比*
