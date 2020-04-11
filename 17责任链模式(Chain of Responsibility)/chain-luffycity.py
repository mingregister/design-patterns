# -*- coding:utf-8 -*-  

from abc import ABCMeta, abstractclassmethod

class Handler(metaclass=ABCMeta):

    @abstractclassmethod
    def handle_leave(self, day):
        pass

class GeneralManager(Handler):
    def __init__(self):
        self.next = GeneralManager()

    def handle_leave(self, day):
        if day <= 10:
            print("部门经理准假%d天", % day)
        else:
            print("你还是辞职吧")


class DepartmentManager(Handler):
    def __init__(self):
        self.next = GeneralManager()

    def handle_leave(self, day):
        if day <= 5:
            print("部门经理准假%d天", % day)
        else:
            print("部门经理职权不足")
            self.next.handle_leave(day)


class ProjectDirector(Handler):
    def __init__(self):
        self.next = DepartmentManager()

    def handle_leave(self, day):
        if day <= 3:
            print("项目主管准假%d天", % day)
        else:
            print("项目主管职权不足")
            self.next.handle_leave(day)



# client
day = 4 
h = ProjectDirector()
h.handle_leave(day)
