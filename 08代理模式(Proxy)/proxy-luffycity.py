# -*- coding:utf-8 -*-
# author:mingregister
# date：2020-04-11,17:56 

from abc import ABCMeta, abstractclassmethod

class Subject(metaclass=ABCMeta):
    @abstractclassmethod
    def get_content(self):
        pass 

    @abstractclassmethod
    def set_content(self, content):
        pass 

class RealSubject(Subject):
    def __init__(self, filename):
        self.filename = filename 

        with open(filename, 'r', encoding='utf-8') as f:
            print('开始读取文件内容...')
            self.content = f.read()

    def get_content(self):
        return self.content

    def set_content(self, content):
        with open(self.filename, 'a+', encoding='utf-8') as f:
            f.write(content)

# subj = RealSubject("test.txt")
# subj.get_content()   # 这个时候，即使用户不执行这个命令，test.txt的内容都已经被读出来了，而且占用了内存

class VirtualProxy(Subject):
    def __init__(self, filename):
        self.filename = filename 
        self.subj = None
    
    def get_content(self):            # 这个逻辑有问题的，会读取不到最新的内容。
        if not self.subj:
            self.subj = RealSubject(self.filename)
        return self.subj.get_content()

    def set_content(self, content):    # 这个逻辑有问题的，会读取不到最新的内容。
        if not self.subj:
            self.subj = RealSubject(self.filename)
        return self.subj.set_content(content)

class ProtectProxy(Subject):
    def __init__(self, filename):
        self.subj = RealSubject(filename)

    def get_content(self):     
        return self.subj.get_content()

    def set_content(self, content):
        raise PermissionError("无写入权限")

subj = RealSubject("test.txt")


print('------------------------------')
vsubj = VirtualProxy("test.txt")
print(vsubj.get_content())

print('------------------------------')
vsubj.set_content('testing ....')
print(vsubj.get_content())



print('------------------------------')
psubj = ProtectProxy("test.txt")
psubj.set_content("kkkkk")
