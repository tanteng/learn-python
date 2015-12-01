# -*- coding: utf-8 -*-

# Python hasattr判断是否存在属性

class Test:

    product11 = ['d']

    def __init__(self):
        pass

    def product(self, a, b):
        return a * b

    def is_exists(self):
       print(hasattr(self, 'product'))


test = Test()
test.is_exists()


"""
dir(test):
['__doc__', '__init__', '__module__', 'is_exists', 'product', 'product11']
"""