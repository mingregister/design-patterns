"""
Control write access to class attributes.
Separate data from methods that use it.
Encapsulate class data initialization.
"""


class DataClass:
    """
    Hide all the attributes.
    """

    def __init__(self):
        self.value = None

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if self.value is None:
            self.value = value
        else: 
            print('set failed!!!')


class MainClass:
    """
    Initialize data class through the data class's constructor.
    """

    attribute = DataClass()

    def __init__(self, value):
        self.attribute = value
        print(id(self.attribute))       # 257560896  他们竟然是同一个东西。
        print(id(MainClass.attribute))  # 257560896


def main():
    m = MainClass(True)
    m.attribute = False
    print(m.attribute)  # True


if __name__ == "__main__":
    main()