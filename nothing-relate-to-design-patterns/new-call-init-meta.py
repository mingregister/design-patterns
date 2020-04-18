# -*- coding:utf-8 -*-
# author: mingregister
# date：2020-04-18,22:51 
# python 3.8.2

from __future__ import annotations


class MetaPerson(type):

    def __new__(cls, name, parents, dct):
        print("i am in MetaPerson new")
        return super(MetaPerson, cls).__new__(cls, name, parents, dct)

    def __call__(cls, *args, **kwargs):
        print('i am in MetaPerson call')
        return super().__call__(*args, **kwargs)


class person(metaclass=MetaPerson):
    def __init__(self, name: string) -> None:
        self.name = name
        print('init')

    def __call__(self):
        print('call')


    def __str__(self):
        return('str')

if __name__ == '__main__':
    m = person('zmhuang')

    m()

    print(m)