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

    # 注释了__get__和__set__方法，self.attribute和MainClass.attribute也不是同一个东西了。
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if self.value is None:
            self.value = value
        else: 
            print('set failed!!!')
            
    
    # # descriptors are invoked by the __getattribute__() method
    # # overriding __getattribute__() prevents automatic descriptor calls
    # # object.__getattribute__() and type.__getattribute__() make different calls to __get__().
    # # data descriptors always override instance dictionaries.
    # # non-data descriptors may be overridden by instance dictionaries.
    # def __getattribute__(self, name):
    #    print('haha ____getattribute__')
    #    return super().__getattribute__(name)


class MainClass:
    """
    Initialize data class through the data class's constructor.
    """

    # https://python3-cookbook.readthedocs.io/zh_CN/latest/c08/p09_create_new_kind_of_class_or_instance_attribute.html
    # https://docs.python.org/3/howto/descriptor.html
    # 为了使用一个描述器，需将这个描述器的实例作为类属性放到一个类的定义中
    attribute = DataClass()
    # attribute = False   # 改成这样，self.attribute和MainClass.attribute就不是同一个东西了。

    def __init__(self, value):
        # The default behavior for attribute access is to get, set, or delete the attribute 
        # from an object’s dictionary. For instance, a.x has a lookup chain starting with a.__dict__['x'], 
        # then type(a).__dict__['x'], and continuing through the base classes of type(a) excluding metaclasses. 
        # If the looked-up value is an object defining one of the descriptor methods, 
        # then Python may override the default behavior and invoke the descriptor method instead. 
        # Where this occurs in the precedence chain depends on which descriptor methods were defined.
        self.attribute = value
        print(id(self.attribute))       # 257560896  他们竟然是同一个东西。
        print(id(MainClass.attribute))  # 257560896

 


def main():
    m = MainClass(True)
    m.attribute = False
    print(m.attribute)  # True

    m2 = MainClass(True)              # 257560896
    m2.attribute = False              # 257560896
    print(m2.attribute)

if __name__ == "__main__":
    main()