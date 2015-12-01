# -*- coding: utf-8 -*-

# Python面向对象：类，类的方法，类方法，静态方法

class Person(object):
    def __init__(self):
        print('init')

    @staticmethod
    def sayHello(hi):
        if hi is None:
            hi = 'hello'
        print(hi)

    @classmethod
    def hi(cls,msg):
        print(msg)
        print(dir(cls))

    # 一般类的方法
    def hobby(self,hobby):
        print(hobby)

# 调用静态方法，不用实例化
Person.sayHello('hi')
Person.hi('Hi!')

# 实例化类调用普通方法,__init__在这里触发
person = Person()
person.hobby('football')


"""
输出：
hi
Hi!
['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof_
_', '__str__', '__subclasshook__', '__weakref__', 'hi', 'hobby', 'sayHello']
init
football

其中def hi(cls)这个类方法，cls表示类自身，所以输出跟dir(person)是一样的。

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