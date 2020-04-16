# -*- coding:utf-8 -*-
# author: mingregister
# date：2020-04-16,19:02 

from abc import ABCMeta, abstractclassmethod


class Command(metaclass=ABCMeta):
    @abstractclassmethod
    def execute(self, *args, **kwargs):
        pass

class Restaurant():
    def __init__(self,TotalDishes, CleanedDishes):
        self.TotalDishes = TotalDishes
        self.CleanedDishes = CleanedDishes

    def MakePizza(self, n):
        return MakePizzaCommand(n, self)

    def MakeSalad(self, n):
        return MakeSaladCommand(n, self)

    def CleanDishes(self):
        return CleanDishesCommand(self)

class MakePizzaCommand(Command):
    def __init__(self, n, restaurant):
        self.n = n
        self.restaurant = restaurant

    def execute(self, *args, **kwargs):
        self.restaurant.CleanedDishes -= self.n
        # 这些print都可以改成日志记录的.
        print("made %s pizzas" % self.n)

class MakeSaladCommand(Command):
    def __init__(self, n, restaurant):
        self.n = n
        self.restaurant = restaurant

    def execute(self, *args, **kwargs):
        self.restaurant.CleanedDishes -= self.n
        print("made %d salads" % self.n)

class CleanDishesCommand(Command):
    def __init__(self, restaurant):
        self.restaurant = restaurant

    def execute(self, *args, **kwargs):
        self.restaurant.CleanedDishes = self.restaurant.TotalDishes
        print("dishes cleaned")


class Cook():
    def __init__(self, commands=None):
        # 这个逻辑也没有什么必要，但是留着吧.
        if commands is not None:
            self.commands = commands
        else:
            raise ValueError("None")

    def executeCommands(self):
        for c in self.commands:
            c.execute()

# 对于python来说，这个函数什么必要.
def NewResteraunt():
    totalDishes = 10
    CleanedDishes = totalDishes
    return Restaurant(totalDishes, CleanedDishes)

if __name__ == '__main__':
    r = NewResteraunt()
    
    # 这里是初始化了很多类的，有办法延时加载么?
    tasks = [r.MakePizza(2),
             r.MakeSalad(1),
             r.MakePizza(3),
             r.CleanDishes(),
             r.MakePizza(4),
             r.CleanDishes()
            ]


    # 不够优雅.
    tasks1 = [tasks[0], tasks[2], tasks[4]]
    tasks2 = [task for task in tasks if task not in tasks1]

    cooks = [Cook(tasks1), Cook(tasks2)]

    for i, c in enumerate(cooks):
        print("cook %d :" %i)
        c.executeCommands()
