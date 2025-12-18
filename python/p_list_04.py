# python 列表(数组)

print('列表定义:')
list0 = []
print(list0)
list1 = [1, 2, 3]
print(list1)
list2 = list((1, 2, 3))
print(list2)
list3 = list(range(1, 11)) # 创建一个列表，包含 1 到 10 的数字
print(list3)

print('列表 添加元素')
li = []
print(li)
li.append(1)
print(li)
li.append(3)
print(li)

print('列表 删除元素')
li = [1, 2, 3, 4, 5]
print(li)
li.pop() # 删除最后一个元素
print(li)
del li[0] # 删除第一个元素
print(li)
li.remove(3) # 删除值为 3 的元素
print(li)

print('列表边界')
li = [1, 2, 3, 4, 5]
print(li[0])
print(li[-1])
print(li[1:3])
# print(li[30]) # 索引越界，程序会报错

print('列表 连接')
li1 = [1, 2, 3]
li2 = [4, 5, 6]
print(li1)
print(li2)

li1.extend(li2)
print(li1)

li1 = [1, 3, 5]
print(li1 + [2, 4, 6])

print('列表 搜索')
li1 = [30, 70, 13, 40, 75, 103, 98, 65]
print(li1.index(13)) # 搜索值为 13 的元素索引
print(li1.index(103, 1, 8)) # 搜索值为 103 的元素索引，索引范围是 1 到 8
print(li1.index(103, 4)) # 搜索值为 103 的元素索引，索引范围是 4 到末尾

print('列表 生成')
li = list(filter(lambda x: x % 2 == 1, range(1, 30)))
print(li)

li = [ x ** 2 for x in range(1, 30) if x % 2 != 1]
print(li)

li = [x for x in [1, 2, 3, 4, 5] if x % 2 == 1]
print(li)

print('列表 切片')
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(li[2:5]) # 索引 2 到 5， [2, 5) = 2, 3, 4 这三个索引
print(li[-5: -2]) # 索引 -5 到 -2，(-5, -2] = -4, -3, -2 这三个索引

# 索引省略
print(li[: 4]) # 索引 0 到 4， [0, 4) = 0, 1, 2, 3 这四个索引]
print(li[0:4])
print(li[4:]) # 索引 4 到末尾， [4, 10) = 4, 5, 6, 7, 8, 9 这六个索引]
print(li[4:len(li)]) # 索引 4 到末尾， [4, 10) = 4, 5, 6, 7, 8, 9 这六个索引]

print(li)
print(li[:])

# 间隔索引 step
print(li[::])
print(li[0:6:2]) # 索引 0 到 6，间隔 2
print(li[1:6:2]) # 索引 1 到 6，间隔 2
print(li[6:0: -2]) # 索引 6 到 0，间隔 -2
print(li)
print(li[::-1]) # 索引 0 到末尾，间隔 -1，倒转

print('列表 排序和反转')
li = [13, 10, 25, 2, 34]
print(li)
li.sort()
print(li)
li.reverse()
print(li)

print('列表 计数')
li = [1, 3, 5, 1, 5, 4, 1, 10, 8]
print("count 5：" + str(li.count(5)))


print('列表 填充和重复')
li = [1, 2, 3]
print(li * 3)
print(li + [4, 5, 6])
print(li + li)
print(['repeat'] * 5)
