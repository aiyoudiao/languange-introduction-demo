# Python 类和继承

print('定义')

class Person_1:
    pass
my = Person_1() # 创建对象

print('构造函数')

class Animal_1:
    def __init__(self, voice):
        self.voice = voice

cat = Animal_1('喵喵喵')
print(cat.voice)

dog = Animal_1('汪汪汪')
print(dog.voice)


print('方法')
class Dog_1:
    def bark(self):
        print('汪汪汪')

dog = Dog_1()
dog.bark()

print('类变量')
class Dog_2:
    voice = '汪汪汪'
print(Dog_2.voice)
d = Dog_2()
print(d.voice)

print('super()函数')
class Animal_2:
    def print_test(self):
        print('animal test')
class Cat_2(Animal_2):
    def print_test(self):
        print('cat test')
        super().print_test()
cat_2 = Cat_2()
cat_2.print_test()

print('__repr__()方法')
class Employee_1:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Employee_1(name={self.name})'
zs = Employee_1('zs')
print(zs)

print('用户自定义的异常')
class MyCustomError(Exception):
    pass

print('多态性')
class Animal_3:
    def print_self(self):
        print('animal 3')
class Cat_3(Animal_3):
    def print_self(self):
        print('cat 3')

animal_3 = Animal_3()
cat_3 = Cat_3()
animal_3.print_self()
cat_3.print_self()

print('重写')
class Animal_4:
    def print_self(self):
        print('animal 4')
class Cat_4(Animal_4):
    def print_self(self):
        print('cat 4')
        # super().print_self()
cat_4 = Cat_4()
cat_4.print_self()

print('抽象类')
from abc import ABC, abstractmethod
class Animal_5(ABC):
    @abstractmethod
    def print_self(self):
        pass
    @abstractmethod
    def print_self_2(self):
        pass

class Cat_5(Animal_5):
    def print_self(self):
        print('cat 5')
    def print_self_2(self):
        print('cat 5_2')

cat_5 = Cat_5()
cat_5.print_self()

print('继承')
class Animal_6:
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs
class Dog_6(Animal_6):
    def sound(self):
        print('汪汪汪')

dog_6 = Dog_6('旺财', 4)
print(dog_6.name, dog_6.legs)
dog_6.sound()
