def hellocounter (name):
    count=[0]
    def counter():
        count[0]+=1
        print('Hello,',name,',',count[0],' access!')
    return counter

hello = hellocounter('ma6174')
hello()
hello()
hello()

def make_adder(addend):
    def adder(augend):
        return augend + addend
    return adder

p = make_adder(23)
q = make_adder(44)

print(p(100))
print(q(100))
