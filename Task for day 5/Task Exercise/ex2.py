# Create a class cal2 that will calculate area of a circle. Create setdata()
# method that should take radius from the user. Create area() method
# that will calculate area . Create display() method that will display area .

class Cal2:
    radius=0
    def setdata(self):
        r = int(input("Enter radius: "))
        self.radius=r
    
    def display(self):
        area = 3.14*self.radius * self.radius
        print("sum is ",area)

c = Cal2()
c.setdata()
c.display()