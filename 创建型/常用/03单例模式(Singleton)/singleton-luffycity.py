# -*- coding:utf-8 -*-
# author: mingregister
# date：2020-04-13,22:18 

class Singleton:
    def __new__(cls, *args, **kwargs):
        '''
        If __new__() does not return an instance of cls, 
        then the new instance’s __init__() method will not be invoked.
        '''
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        # 我也不能把它return成其他类吧，不然单例模式不就没有意义了。
        return cls._instance

class MyClass(Singleton):
    def __init__(self, a):
        self.a = a 

# 这里即使返回的是*同一个实例*，但是还是会再初始化一次?
a = MyClass(10)
# b的init方法是被执行了的。
b = MyClass(20)      # 这里是有问题的，应该这里就不能再实例化，即：print(b.a)应该是10才对。

print(a.a)   # 20
print(b.a)   # 20
print(id(a), id(b))

