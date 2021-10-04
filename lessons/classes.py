class MyClass:
    var1 = 1

    @classmethod
    def update(cls, value):
        cls.var1 += value

    def __init__(self):
        pass

a = MyClass()
print(a.var1)
a.update(1)
print a.var1
b = MyClass()
print(b.var1)
