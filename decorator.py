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

关于装饰器的具体概念，参见：
http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386819879946007bbf6ad052463ab18034f0254bf355000
"""
