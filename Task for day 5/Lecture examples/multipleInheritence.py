class Demo:

    def __init__(self):
        print("parent constructor")

    def func1(self):
        print("func1")

class Demo1:
    def func2(self):
        print("func2")

    def __init__(self):
        print("child constructor")

class Demo2(Demo,Demo1):
    def func3(self):
        print("func3")

d2=Demo2()
d2.func1()
d2.func2()
d2.func3()