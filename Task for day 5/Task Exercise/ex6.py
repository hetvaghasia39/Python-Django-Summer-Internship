# Create a class cal5 that will calculate area of a rectangle. Create
# constructor method which has two parameters .Create calArea()
# method that will calculate area of a rectangle. Create display() method
# that will display area of a rectangle.

class Cal5:
    len,width = 0,0
    area = 0
    def __init__(self,a,b):
        self.len,self.width = a,b

    def calArea(self):
        self.area = self.len*self.width
    
    def display(self):
        print("area of rectangle is ",self.area)

len = int(input("Enter length "))
width = int(input("Enter width: "))
cal = Cal5(len,width)
cal.calArea()
cal.display()