# encoding:utf-8

# -*- Python3可变参数 -*-

import webbrowser

def alias(*args, **kwargs):
    print('args=', args)
    print('kwargs=', kwargs)
    return

alias(3, 23, 3, 3,a='hello',b=3,c='C')

"""
输出：
args= (3, 23, 3, 3)
kwargs= {'b': 3, 'c': 'C', 'a': 'hello'}

小结：
*args表示任何多个无名参数，它是一个tuple
**kwargs表示关键字参数，它是一个dict
"""

# 具体参考资料
webbrowser.open('http://www.tantengvip.com/2015/07/python-args-kwargs/', 1)
