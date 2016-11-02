class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

x = MyClass()
print(x.i)
print(x.f())
print(x.f() + "!!")
print(str(30) + "years old")


class MyClass_2:
    """The 2nd example of class"""
    i = 12345

    def f(self, name):
        return ("hello " + name)

    def g(self, name):
        print(name + " is " + str(self.i) + " yen.")

y = MyClass_2()
print(y.f("Nezasa"))
y.g("Nezasa")


class MyClass_3:
    """The 3rd example of class"""

    def __init__(self, name):
        self.label = name
        print("hello " + name)

z = MyClass_3("Nezasa")
print(z.label)
z.__init__("Sasatch")
print(z.label)


class Complex:

    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    def print_cmpl3(self):
        print("%.3f + %.3f i" % (self.r, self.i))

    def print_cmpl5(self):
        print("%.5f + %.5f i" % (self.r, self.i))

w = Complex(1.23333, -3.122222)
w.print_cmpl3()
w.print_cmpl5()
