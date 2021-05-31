#Overeiding method
class Demo:
    def func(self):
        print("Demo class")

class Demo1(Demo):
    def func(self):
        print("Demo1 class")

d = Demo1()
d.func()