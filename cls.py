# -*- coding: utf-8 -*-

# Python 的cls

class demo(object):
    def foo(cls):
        print(dir(cls))

demo = demo()
demo.foo()

"""
demo.foo()输出的结果跟dir(demo)的结果一样：
['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof_
_', '__str__', '__subclasshook__', '__weakref__', 'foo']
"""