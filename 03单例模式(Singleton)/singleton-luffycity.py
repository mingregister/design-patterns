# -*- coding:utf-8 -*-
# author: mingregister
# date：2020-04-13,22:18 

class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

class MyClass(Singleton):
    def __init__(self, a):
        self.a = a 

# 这里即使返回的是*同一个实例*，但是还是会再初始化一次?
a = MyClass(10)
b = MyClass(20)

print(a.a)   # 20
print(b.a)   # 20
print(id(a), id(b))

