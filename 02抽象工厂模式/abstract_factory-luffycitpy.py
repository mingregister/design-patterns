# -*- coding:utf-8 -*-  

from abc import ABCMeta, abstractclassmethod

#  ----------抽象产品-----------------
class PhoneShell(metaclass=ABCMeta):
    @abstractclassmethod    
    def show_shell(self):
        pass

class CPU(metaclass=ABCMeta):
    @abstractclassmethod    
    def show_cpu(self):
        pass

class OS(metaclass=ABCMeta):
    @abstractclassmethod    
    def show_os(self):
        pass


#  ----------抽象工厂-----------------
class PhoneFactory(metaclass=ABCMeta):
    @abstractclassmethod    
    def make_shell(self):
        pass

    @abstractclassmethod    
    def make_cpu(self):
        pass

    @abstractclassmethod    
    def make_os(self):
        pass


#  ----------具体产品：实现抽象产品---------------
class SmallShell(PhoneShell):
    def show_shell(self):
        print("普通手机小手机壳")

class BigShell(PhoneShell):
    def show_shell(self):
        print("普通手机大手机壳")

class AppleShell(PhoneShell):
    def show_shell(self):
        print("苹果手机壳")

class SnapDragonCPU(CPU):
    def show_cpu(self):
        print("骁龙CPU")

class MediaTekCPU(CPU):
    def show_cpu(self):
        print("联发科CPU")

class AppleCPU(CPU):
    def show_cpu(self):
        print("苹果CPU")

class Android(OS):
    def show_os(self):
        print("Addroid os")

class IOS(OS):
    def show_os(self):
        print("IOS")



#  ----------具体工厂：实现抽象工厂---------------
class MiFactory(PhoneFactory):

    def __init__(self):
        print(self.__class__.__name__)

    def make_cpu(self):
        return SnapDragonCPU()

    def make_os(self):
        return Android()

    def make_shell(self):
        return BigShell()

class HuaweiFactory(PhoneFactory):
    def __init__(self):
        print(self.__class__.__name__)

    def make_cpu(self):
        return MediaTekCPU()

    def make_os(self):
        return Android()

    def make_shell(self):
        return SmallShell()

class IPhoneFactory(PhoneFactory):
    def __init__(self):
        print(self.__class__.__name__)

    def make_cpu(self):
        return AppleCPU() 

    def make_os(self):
        return IOS()

    def make_shell(self):
        return AppleShell()


# -----------客户端-------------------
class Phone:
    def __init__(self, cpu, os, shell):
        self.cpu = cpu
        self.os = os
        self.shell = shell

    def show_info(self):
        print("手机信息")
        self.cpu.show_cpu()
        self.os.show_os()
        self.shell.show_shell()

def make_phone(factory):
    cpu = factory.make_cpu()
    os = factory.make_os()
    shell = factory.make_shell()
    return Phone(cpu, os, shell)

p1 = make_phone(IPhoneFactory())
p1.show_info()
