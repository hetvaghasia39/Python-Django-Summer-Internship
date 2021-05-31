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

d1=Demo1()
d1.func1()
d1.func2()

d2=Demo2()
d2.func1()
d2.func3()