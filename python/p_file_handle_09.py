# Python 文件处理

print('逐行读取文件：')
with open('./python/file/my_file.txt', encoding='utf-8') as file:
    for line in file:
        print(line)

file = open('./python/file/my_file.txt', 'r', encoding='utf-8')
for i, line in enumerate(file, start = 1):
    print(f'No {i} => {line}')

print('读写整个文件')
contents = {'zs': 18, 'ls': 19, 'ww': 20 }
print(contents)
with open('./python/file/my_file_2.txt', 'w+', encoding='utf-8', newline='') as file:
    file.write(str(contents))

with open('./python/file/my_file_2.txt', 'r+', encoding='utf-8') as file:
    comments = file.read()
print(comments)

print('读写整个json')
import json
contents = {
    'name': '张三',
    'age': 18,
    'sex': '男',
    'hobby': ['football', 'basketball'],
    'married': False,
    'birthday': '1990-01-01'
}
with open('./python/file/my_file_3.json', 'w+', encoding='utf-8') as file:
    file.write(json.dumps(contents))
with open('./python/file/my_file_3.json', 'r+', encoding='utf-8') as file:
    contents = json.loads(file.read())
print(contents)

print('读写二进制文件')
with open('./python/file/my_file_4.jpg', 'rb') as file:
    contents = file.read()
with open('./python/file/my_file_4.png', 'wb') as file:
    file.write(contents)

print('读写csv文件')
import csv
contents = [
    ['name', 'age', 'sex'],
    ['张三', 18, '男'],
    ['李四', 19, '女'],
    ['王五', 20, '男']
]
with open('./python/file/my_file_5.csv', 'w+', encoding='utf-8', newline= '') as file:
    writer = csv.writer(file)
    writer.writerows(contents)
    writer.writerow(['张三', 18, '男'])
with open('./python/file/my_file_5.csv', 'r+', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# print('读写excel文件')

# import xlrd
# book = xlrd.Workbook(encoding='utf-8')
# sheet = book.add_sheet('Sheet1')
# sheet.write(0, 0, 'name')
# sheet.write(0, 1, 'age')
# sheet.write(0, 2, 'sex')
# sheet.write(1, 0, '张三')
# sheet.write(1, 1, 18)
# sheet.write(1, 2, '男')
# book.save('./python/file/my_file_6.xlsx')

# import xlrd
# book = xlrd.open_workbook('./python/file/my_file_6.xlsx')
# sheet = book.sheet_by_name('Sheet1')
# print(sheet.name, sheet.nrows, sheet.ncols)
# for i in range(sheet.nrows):
#     print(sheet.row_values(i))
#     print(sheet.cell_value(i, 0), sheet.cell_value(i, 1), sheet.cell_value(i, 2))
#     print(sheet.row(i))
#     print(sheet.col_values(i))
#     print(sheet.col(i))
#     print(sheet.cell(i, 0), sheet.cell(i, 1), sheet.cell(i, 2))

print('删除文件')
import os
os.remove('./python/file/my_file_4.png')

print('检查和删除')
import os
if os.path.exists('./python/file/my_file_4.png'):
    os.remove('./python/file/my_file_4.png')
else:
    print('文件不存在')

print('删除文件夹')
from os import mkdir, rmdir, path
if not path.exists('./python/file/my_file_dir'):
    mkdir('./python/file/my_file_dir')
else:
    rmdir('./python/file/my_file_dir')
