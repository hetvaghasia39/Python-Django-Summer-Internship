# default costructor & parameterized constructor

class Demo:
    def myFunction(self):
        print("this is class function")

    def show(self,name):
        print("parameter is ",name)

    '''def __init__(self):
        print("this is default constructor")'''

    def __init__(self,surname):
        print("this is constructor")
        print("surname is ",surname)

d1 = Demo("Vaghasia")
d1.myFunction()
d1.show('Het')