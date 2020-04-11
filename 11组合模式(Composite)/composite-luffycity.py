# coding: utf-8 

from abc import ABCMeta, abstractclassmethod

# 抽象组件
class Graphic(metaclass=ABCMeta):
    @abstractclassmethod
    def draw(self):
        pass 

# 叶子组件
class Point(Graphic):
    def __init__(self, x, y):
        self.x = x
        self.y = y 

    def __str__(self):
        return "点(%s, %s)" %(self.x, self.y)

    def draw(self):
        print(str(self))    

# 叶子组件
class Line(Graphic):
    def __init__(self, p1, p2):
        self.p1 = p1 
        self.p2 = p2 

    def __str__(self):
        return "线段[%s, %s]" % (self.p1, self.p2)

    def draw(self):
        print(str(self)) 

# 复合组件
class Picture(Graphic):
    def __init__(self, iterable):
        self.children = []
        for g in iterable:
            self.add(g)

    def add(self, graphic):
        self.children.append(graphic)

    def draw(self):
        print("--------复合图形--------------------")
        for  g in self.children:
            g.draw()
        print("--------复合图形--------------------")

l = Line(Point(1,1), Point(2,2))
l.draw()
# print(l)

p1 = Point(2,3)
l1 = Line(Point(3,4), Point(6,7))
l2 = Line(Point(1,3), Point(7,8))
pic1 = Picture([p1, l1, l2])
pic1.draw()