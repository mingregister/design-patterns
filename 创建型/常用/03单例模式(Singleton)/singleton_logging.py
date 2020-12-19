# -*- coding:utf-8 -*-
# author: mingregister
# date：2020-07-16,05:37 
# python 3.8.3


# 这也是实现单例模式的一种方法?通过类属性? 有什么优缺点?
# 以下内容写在__init__.py文件中，在每次import/getLogger 的时候，都会返回同一个manager实例



class Filterer(object):
    def __init__(self):
        """
        Initialize the list of filters to be an empty list.
        """
        self.filters = []

class Logger(Filterer):
    def __init__(self, name, level=NOTSET):
        """
        Initialize the logger with a name and an optional level.
        """
        Filterer.__init__(self)
        self.name = name
        self.level = _checkLevel(level)
        self.parent = None
        self.propagate = True
        self.handlers = []
        self.disabled = False
        self._cache = {}


class RootLogger(Logger):
    """
    A root logger is not that different to any other logger, except that
    it must have a logging level and there is only one instance of it in
    the hierarchy.
    """
    def __init__(self, level):
        """
        Initialize the logger with the name "root".
        """
        Logger.__init__(self, "root", level)

    ...

class Manager(object):
    def __init__(self, rootnode):
        self.root = rootnode
        self.disable = 0
        self.emittedNoHandlerWarning = False
        self.loggerDict = {}
        self.loggerClass = None
        self.logRecordFactory = None

     def getLogger(self, name):
        rv = None
        if not isinstance(name, str):
            raise TypeError('A logger name must be a string')
        _acquireLock()
        try:
            if name in self.loggerDict:
                rv = self.loggerDict[name]
                if isinstance(rv, PlaceHolder):
                    ph = rv
                    rv = (self.loggerClass or _loggerClass)(name)
                    rv.manager = self
                    self.loggerDict[name] = rv
                    self._fixupChildren(ph, rv)
                    self._fixupParents(rv)
            else:
                rv = (self.loggerClass or _loggerClass)(name)
                rv.manager = self
                self.loggerDict[name] = rv
                self._fixupParents(rv)
        finally:
            _releaseLock()
        return rv
   

root = RootLogger(WARNING)
Logger.root = root
# Q: 如果第二个文件再import怎么办? 是再import的时候，并没有*实际执行import*么?
# A: 是的，第二次文件中再import的时候，应该是真的没有*实际执行import*，在两个文件中id(logging)是可以看到同一个输出的，
#    which means, 他们是同一个对象。
Logger.manager = Manager(Logger.root)


def getLogger(name=None):
    """
    Return a logger with the specified name, creating it if necessary.

    If no name is specified, return the root logger.
    """
    if name:
        return Logger.manager.getLogger(name)
    else:
        return root