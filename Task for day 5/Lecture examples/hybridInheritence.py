class Demo:

    def __init__(self):
        print("parent constructor")

    def func1(self):
        print("func1")

class Demo1(Demo):
    def func2(self):
        print("func2")

class Demo2(Demo):
    def func3(self):
        print("func3")

class Demo3(Demo1,Demo2):
    def func4(self):
        print("func4")

d = Demo3()
d.func1()
d.func2()
d.func3()
d.func4()