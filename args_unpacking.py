# -*- coding: utf-8 -*-

# 使用tupple或dict传参的技巧

def product(a, b):
    print(str(a) + '*' + str(b))
    return a * b

argument_tuple = (1, 1)
argument_dict = {'a': 1, 'b': 1}

print(product(*argument_tuple)) # 这里用*解析tupple类型的变量作为product的参数
print(product(**{'b':4,'a':3})) # 这里用**解析dict类型的变量作为product的参数
