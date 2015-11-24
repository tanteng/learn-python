# encoding:utf-8

# -*- Python单例模式示例 -*-

class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

if __name__ == '__main__':
    a = Singleton() 
    b = Singleton() 
    print(id(a))
    print(id(b))
