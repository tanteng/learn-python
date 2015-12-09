# coding=utf-8

# 定义一个装饰器
def mydecorator(func):
    def wrapper(*args,**kw):
        print('hi,now is:')
        return func(*args,**kw)
    return wrapper

# 使用装饰器
@mydecorator
def now():
    print('2015-12-9')

now()

"""
D:\learn-python>python decorator.py
hi,now is:
2015-12-9
"""
