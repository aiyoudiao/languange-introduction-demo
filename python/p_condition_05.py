# 判断

print('判断 if else')
# number = int(input('请输入数字：'))
number = 10
if number > 0:
    print('数字大于0')
else:
    print('数字小于等于0')

print('判断 if elif else')
number = 0
if (number > 0):
    print('数字大于0')
elif (number == 0):
    print('数字等于0')
else:
    print('数字小于0')

print('判断 三目运算符')
scope = 60
tip = '合格' if scope >= 60 else '不合格'
print(tip)

