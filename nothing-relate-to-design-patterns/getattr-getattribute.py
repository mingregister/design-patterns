# -*- coding:utf-8 -*-
# author: mingregister
# date：2020-04-19,20:16 
# python 3.8.2


class Student(object):
    def __init__(self, name1):
        self.name0 = name1

    def __call__(self, bitch):
        print('__call__ says 1: My name is %s.' % self.name0)
        print('__call__ says 2: hello %s'% bitch)

    def __getattr__(self, name3):    # 其实是调用了getattr函数?!?
        print('__getattr__ says: The attribute *%s* you are get is not exist!!!'% name3)

    def __setattr__(self, name4, value4):
        # # 如果这里什么都不写，会导致'__call__ says 1'的self.name0是None
        # setattr(self, name4, value4)  # 这种写法会导致无限递归，请看: 《 魔法方法(二)》
        # self.__dict__[name4] = value4                          # 这种写法效果和super一样，不会引起无限递归!!!
        super().__setattr__(name4,value4)                        # 留意这里是否注释的区别!!!
        print('__setattr__ 定义当一个属性被设置时的行为--> %s=%s'%(name4,value4))

    def __delattr__(self, name5):
        print('__delattr__ oh!!! what the fxck, you are deleting *%s*'%name5)

    def myprint(self):
        print('myprint attribute exists')

    # def __getattribute__(self, school):
    #     print('__getattribute__ says: 当类的任何属性被访问时就会触发。')

    # @property
    # def myprint_property(self):
    #     print('myprint_prperty attribute exists')

if __name__ == "__main__":
    s = Student('lido')
    s('bitch')
    s.this_attr_does_not_exist
    s.myprint()
    del s.myprint