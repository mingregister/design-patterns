# -*- coding:utf-8 -*-
# author: mingregister
# date：2020-04-19,14:59 
# python 3.8.2


from collections.abc import Iterator, Iterable 
from __future__ import annotations

class MyIterable(Iterable):
    def __init__(self, collection):
        self.collection = collection
        print("init")

    def __iter__(self) -> Iterator :
        print("i am MyIterable.__iter__ ")
        return MyIterator(self.collection)

class MyIterator(Iterator):
    def __init__(self, collection: Iterable):
        self._collection = collection
        print("i am MyIterator init")

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value
