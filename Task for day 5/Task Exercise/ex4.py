# Create a class cal4 that will calculate square of a number. Create
# setdata() method which has one parameters that contain number.
# Create display() method that will calculate sum.(Function should
# return value)

class Cal4:
    n = 0 # number
    def setdata(self,a):
       self.n = a

    def display(self):
        square = self.n*self.n
        print("square of ",self.n," is ",square)

n = int(input("Enter a number: "))
cal = Cal4()
cal.setdata(n)
cal.display()