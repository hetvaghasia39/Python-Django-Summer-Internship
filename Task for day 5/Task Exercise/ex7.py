# Create a class cal6 that will calculate area of a square. Create setdata()
# method that should take length from the user. Create area() method
# that will calculate area . Create display() method that will display area 

class Cal6:
    side, squareArea = 0,0 # side and area var
    def setdata(self):
        a = int(input("Enter side of square"))
        self.side = a
    
    def area(self):
        self.squareArea = self.side*self.side

    def display(self):
        print("Area of square is ",self.squareArea)

cal = Cal6()
cal.setdata()
cal.area()
cal.display()