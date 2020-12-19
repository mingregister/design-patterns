from __future__ import annotations
from typing import Optional

# https://refactoring.guru/design-patterns/singleton/python/example#example-0

# It’s pretty easy to implement a sloppy Singleton. You just need to hide constructor and implement a static creation method.

# The same class behaves incorrectly in a multithreaded environment. Multiple threads can call the creation method simultaneously and get several instances of Singleton class.

class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instance: Optional[Singleton] = None

    # 这里不是用cls?
    def __call__(cls, *args, **kwargs) -> Singleton:
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        # # If you want to run __init__ every time the class is called, add
        # else:
        #      cls._instances[cls].__init__(*args, **kwargs)
        return cls._instance

    # # *原代码*，我感觉这里有两个问题：
    # #   1. self应该要换成cls，虽然用self也不会造成什么实际的问题。
    # #   2. __call__(self)应该要传入参数，如：__call__(self, *args, **kwargs)，
    # #      否则，在实例化的时候会报如下错误：
    # #             TypeError: __call__() takes 1 positional argument but 2 were given
    # def __call__(self) -> Singleton:
    #     if self._instance is None:
    #         self._instance = super().__call__()
    #     return self._instance


class Singleton(metaclass=SingletonMeta):

    # 这里的init函数要怎么写，不能有么?!?  可以有，是之前的SingletonMeta的__call__方法有错误
    def __init__(self, a):
        self.a = a

    # # 不能继承/覆盖SingletonMeta的__call__方法?
    # def __call__(self):
    #     print('i am in Singleton call')
    #     return super().__call__(*args, **kwargs)

    def some_business_logic(self):
        """
        Finally, any singleton should define some business logic, which can be
        executed on its instance.
        """

        # ...


if __name__ == "__main__":
    # The client code.

    s1 = Singleton('aaaa')
    # s2的init方法是没有被执行的。
    s2 = Singleton('bbbb')   

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")


    print(s1.a)    # aaaa
    print(s2.a)    # aaaa