# -*- coding:utf-8 -*-
# author: mingregister
# date：2020-04-12,23:43 

# AbstractState
class ComputerState(object):
    name = "state"
    allowed = []

    def switch(self, state):
        if state.name in self.allowed:
            print('Current:', self, '=> switch to new state', state)
            self.__class__ = state
        else:
            print('Current:', self, '=> switch to ', state, 'not possible.')
    
    def __str__(self):
        return self.name

# 自定义的状态: ConcreateState
class Off(ComputerState):
    name = "off"
    allowed = ['on', 'suspend', 'hibernate']

class On(ComputerState):
    name = "on"
    allowed = ['off', 'suspend', 'hibernate']

class Suspend(ComputerState):
    name = "suspend"
    allowed = ['on']

class Hibernate(ComputerState):
    name = "hibernate"
    allowed = ['on']

# Context
class Computer(object):
    def __init__(self, model='HP'):
        self.model = model
        self.state = Off()

    def change(self, state):
        self.state.switch(state)

if __name__ == "__main__":
    comp = Computer()
    comp.change(On)
    comp.change(Off)
    comp.change(On)
    comp.change(Suspend)
    comp.change(Hibernate)
    comp.change(On)
    comp.change(Off)
    

