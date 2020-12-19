# coding: utf-8 

from abc import ABCMeta, abstractclassmethod

# # bad instance: 颜色与形状严重耦合在一起了。 如果要加一个*黑色的圆*，很麻烦 。
# class Shape:
#     pass
# class Line(Shape):
#     pass
# class Rectangle(Shape):
#     pass
# class Circle(Shape):
#     pass
# class Redline(Line):
#     pass
# class Greenline(Line):
#     pass
# class Buleline(Line):
#     pass

class Shape(metaclass=ABCMeta):
    def __init__(self, color):
        self.color = color 

    @abstractclassmethod
    def draw(self):
        pass

class Color(metaclass=ABCMeta):
    @abstractclassmethod
    def paint(self, shape):
        pass

class Rectangle(Shape):
    name = "长方形"
    def draw(self):
        self.color.paint(self)

class Circle(Shape):
    name = "圆形"
    def draw(self):
        self.color.paint(self)    # 这个self代表的是Circle，就是下面parint(self, shape)的shape

class Red(Color):
    def paint(self, shape):
        print("红色的%s" % shape.name)

class Green(Color):
    def paint(self, shape):
        print("绿色的%s" % shape.name)

shape = Rectangle(Red())
shape.draw()

shape2 = Circle(Green())
shape2.draw()