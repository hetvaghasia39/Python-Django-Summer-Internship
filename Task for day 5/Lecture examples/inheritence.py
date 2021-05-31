class Demo:

    def __init__(self):
        print("parent constructor")

    def func1(self):
        print("func1")

class Demo1(Demo):
    def func2(self):
        print("func2")

    def __init__(self):
        print("child constructor")

d1=Demo1()
d1.func1()
d1.func2()