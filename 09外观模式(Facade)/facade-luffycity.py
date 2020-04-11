# coding: utf-8 


class CPU:
    def run(self):
        print("CPU开始工作")

    def stop(self):
        print("CPU停止工作") 

class Disk:
    def run(self):
        print("硬盘开始工作")

    def stop(self):
        print("硬盘停止工作") 

class Memory:
    def run(self):
        print("内存开始工作")

    def stop(self):
        print("内存停止工作") 

# Facade
class Computer():
    def __init__(self):
        self.cpu = CPU()
        self.disk = Disk()
        self.memory = Memory()

    def run(self):
        self.cpu.run()
        self.disk.run()
        self.memory.run()

    def stop(self):
        self.cpu.stop()
        self.disk.stop()
        self.memory.stop()


computer = Computer()
computer.run()
computer.stop()
