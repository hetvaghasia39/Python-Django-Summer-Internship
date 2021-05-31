# Create a arith class. The class should have a parameterized constructor
# and methods to add, subtract and multiply two numbers and to return
# the answers.

class Arith:
    n1,n2 = 0,0
    def __init__(self,a,b):
        self.n1,self.n2 = a,b
    
    def add(self):
        add = self.n1 + self.n2
        return add

    def sub(self):
        sub = self.n1 +-self.n2
        return sub

    def mul(self):
        mul = self.n1 * self.n2
        return mul

    def div(self):
        div = self.n1 / self.n2
        return div

a = int(input("enter 1st number: "))
b = int(input("enter 2nd number: "))    
ar = Arith(a,b)
print("Sum is ",ar.add(),"\nDifference is ",ar.sub(),"\nMultiplication is ",ar.mul(),"\nDivision is ",ar.div())