from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List

from typing import Optional

"""
To create an iterator in Python, there are two abstract classes from the built-
in `collections` module - Iterable,Iterator. We need to implement the
`__iter__()` method in the iterated object (collection), and the `__next__ ()`
method in theiterator.
"""

# 单例模式感觉还有坑，不会用。
class SingletonMeta:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(SingletonMeta, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self._count = 0

class Count(SingletonMeta):

    # _count = None

    # def __init__(self):
        # self._count = 0

    def add(self):
        self._count += 1

    def get_count(self):
        return self._count

    def __str__(self):
        return str(self._count)




# 注意下，python这里的继承的是collections.abc.Iterator
# 而且下面继承的是collections.abc.Iterable
class AlphabeticalOrderIterator(Iterator):
    """
    Concrete Iterators implement various traversal algorithms. These classes
    store the current traversal position at all times.
    """

    """
    `_position` attribute stores the current traversal position. An iterator may
    have a lot of other fields for storing iteration state, especially when it
    is supposed to work with a particular kind of collection.
    """
    _position: int = None

    """
    This attribute indicates the traversal direction.
    """
    _reverse: bool = False

    def __init__(self, collection: WordsCollection, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

        print("I am AlphabeticalOrderIterator.__init__: %d" % step_count.get_count())
        step_count.add()

    def __next__(self):
        """
        The __next__() method must return the next item in the sequence. On
        reaching the end, and in subsequent calls, it must raise StopIteration.
        """
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
            print("I am AlphabeticalOrderIterator.__next__: %d" % step_count.get_count())
            step_count.add()
        except IndexError:
            print("I am AlphabeticalOrderIterator.IndexError: %d" % step_count.get_count())
            raise StopIteration()

        return value


# ConcreateAggregate，这个是*可迭代对象*,要实现__iter__方法
class WordsCollection(Iterable):
    """
    Concrete Collections provide one or several methods for retrieving fresh
    iterator instances, compatible with the collection class.
    """

    def __init__(self, collection: List[Any] = []) -> None:
        self._collection = collection
        print("I am WordsCollection.init: %d" % step_count.get_count())
        step_count.add()

    def __iter__(self) -> AlphabeticalOrderIterator:
        """
        The __iter__() method returns the iterator object itself, by default we
        return the iterator in ascending order.
        """
        
        # 这里直接return一个Iterator，在Iterator里面，它会自动调用__next__方法。
        print("I am WordsCollection.__iter__: %d" % step_count.get_count())
        step_count.add()
        return AlphabeticalOrderIterator(self._collection)

    def get_reverse_iterator(self) -> AlphabeticalOrderIterator:

        return AlphabeticalOrderIterator(self._collection, True)

    def add_item(self, item: Any):
        self._collection.append(item)


if __name__ == "__main__":
    # The client code may or may not know about the Concrete Iterator or
    # Collection classes, depending on the level of indirection you want to keep
    # in your program.

    step_count = Count()
    print(step_count.get_count())
    step_count.add()
    print(step_count.get_count())
    step_count2 = Count()
    print(step_count2.get_count())
    

    print(id(step_count)==id(step_count2))

    print("Start: %d" % step_count.get_count())
    step_count.add()

    collection = WordsCollection()
    collection.add_item("First")
    collection.add_item("Second")
    collection.add_item("Third")

    print("Straight traversal:")
    print("\n".join(collection))
    print("")

    print("Reverse traversal:")
    print("\n".join(collection.get_reverse_iterator()), end="")