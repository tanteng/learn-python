def bar(self, y):
    return self.x + y


class Foo(object):
    def __init__(self, x):
        self.x = x

    bar = bar;


foo = Foo(333);
print(foo.bar(3))

#result:336