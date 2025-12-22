# Python 模块

print('模块导入：')
import math
print(math.sqrt(16))
print(math.pow(4, 2))

print('模块别名：')
import math as m
print(m.sqrt(16))
print(m.pow(4, 2))
print(4**2)

print('从一个模块导入')
from math import ceil, floor
print(ceil(10.1))
print(floor(10.1))

print('导入一个模块的全部')
from math import *
print(sqrt(16))
print(pow(4, 2))

print('浏览模块的函数和属性')
import math
print('math => ', dir(math))
import os
print('os => ', dir(os))
import datetime
print('datetime => ', dir(datetime))
import sys
print('sys => ', dir(sys))


