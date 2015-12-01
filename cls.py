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

classmethod：类方法
staticmethod：静态方法

在python中，静态方法和类方法都是可以通过类对象和类对象实例访问。但是区别是：

1.@classmethod 是一个函数修饰符，它表示接下来的是一个类方法，而对于平常我们见到的则叫做实例方法。
类方法的第一个参数cls，而实例方法的第一个参数是self，表示该类的一个实例。

2.普通对象方法至少需要一个self参数，代表类对象实例

3.类方法有类变量cls传入，从而可以用cls做一些相关的处理。并且有子类继承时，调用该类方法时，传入的类变量cls是子类，而非父类。
对于类方法，可以通过类来调用，就像C.f()，有点类似C＋＋中的静态方法, 也可以通过类的一个实例来调用，就像C().f()，这里C()，写成这样之后它就是类的一个实例了。

4.静态方法则没有，它基本上跟一个全局函数相同，一般来说用的很少
"""