# -*- coding:utf-8 -*-
# author: mingregister
# date：2020-04-12,23:43 

# Solution 2: 修改实例的__class__属性。面向对象编程的拥泵不喜欢这种方式，但是技术上还是允许的。并且这种方式的速度也会更快。
class Connection():

    def __init__(self):
        self.new_state(ClosedConnection)

    def new_state(self, newstate):
        self.__class__ = newstate

    def read(self):
        raise NotImplementedError()

    def write(self, data):
        raise NotImplementedError()

    def open(self):
        raise NotImplementedError()

    def close(self):
        raise NotImplementedError()


class ClosedConnection(Connection):

    def read(self):
        raise RuntimeError('Not open')

    def write(self, data):
        raise RuntimeError('Not open')

    def open(self):
        self.new_state(OpenConnection)

    def close(self):
        raise RuntimeError('Already closed')


class OpenConnection(Connection):

    def read(self):
        print('reading')

    def write(self, data):
        print('writing')

    def open(self):
        raise RuntimeError('Already open')

    def close(self):
        self.new_state(ClosedConnection)


if __name__ == "__main__":
    c = Connection()
    c
    # c.read()
    c.open()
    c
    c.read()
    c.write('hello')
    c.close()
    c