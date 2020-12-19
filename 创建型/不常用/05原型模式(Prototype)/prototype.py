# coding: utf-8

import copy
from collections import OrderedDict


class Book:

    def __init__(self, name, authors, price, **rest):
        '''rest的例子有：出版商，长度，标签，出版日期'''
        self.name = name
        self.authors = authors
        self.price = price      # 单位为美元
        self.__dict__.update(rest)

    def __str__(self):
        mylist = []
        ordered = OrderedDict(sorted(self.__dict__.items()))
        for i in ordered.keys():
            mylist.append('{}: {}'.format(i, ordered[i]))
            if i == 'price':
                mylist.append('$')
            mylist.append('\n')
        return ''.join(mylist)


class Prototype:

    def __init__(self):
        self.objects = dict()

    # 用于在一个字典中追踪被克隆的对象。非必需
    def register(self, identifier, obj):
        self.objects[identifier] = obj

    def unregister(self, identifier):
        del self.objects[identifier]

    # attr，用于传递在克隆一个对象时真正需要变更的属性变量。
    def clone(self, identifier, **attr):
        found = self.objects.get(identifier)
        if not found:
            raise ValueError('Incorrect object identifier: {}'.format(identifier))
        obj = copy.deepcopy(found)
        obj.__dict__.update(attr)
        return obj


def main():
    b1 = Book('The C Programming Language', ('Brian W. Kernighan', 'Dennis M.Ritchie'), price=118, publisher='Prentice Hall',
              length=228, publication_date='1978-02-22', tags=('C', 'programming', 'algorithms', 'data structures'))

    prototype = Prototype()
    # 关联cid与b1实例，在下面复制的时候，说明我要复制的是什么实例。
    cid = 'k&r-first'
    prototype.register(cid, b1)
    b2 = prototype.clone(cid, name='The C Programming Language(ANSI)', price=48.99,
                         length=274, publication_date='1988-04-01', edition=2)

    for i in (b1, b2):
        print(i)
    print('ID b1 : {} != ID b2 : {}'.format(id(b1), id(b2)))

if __name__ == '__main__':
    main()
