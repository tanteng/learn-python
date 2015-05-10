def scope_test():
    def do_local():
        spam = "local spam"
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
    def do_global():
        global spam
        spam = "global spam"
 
    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)
 
scope_test()
print("In global scope:", spam)

def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter
    
def make_counter_test():
  mc = make_counter()
  print(mc())
  print(mc())
  print(mc())

make_counter_test()