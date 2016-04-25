def hellocounter (name):
    count=0 #PYTHON 2.x 中，要写count=[0]
    def counter():
        nonlocal count #PYTHON 2.x 中，此行和下一行要换成count[0]+=1
        count+=1
        print('Hello,',name,',',count,' access!')#PYTHON 2.x 中请自觉换成str(count[0])
    return counter

hello = hellocounter('ma6174')
hello()
hello()
hello()

'''
执行结果
>>> hello()
Hello, ma6174 , 1  access!
>>> hello()
Hello, ma6174 , 2  access!
>>> hello()
Hello, ma6174 , 3  access!
'''
##为什么PYTHON 2.x中不直接写count而用list？这是python2的一个bug,如果用count话,会报这样一个错误:
##UnboundLocalError: local variable 'count' referenced before assignment.

def make_adder(addend):
    def adder(augend):
        return augend + addend
    return adder

p = make_adder(23)
q = make_adder(44)

print(p(100))
print(q(100))
