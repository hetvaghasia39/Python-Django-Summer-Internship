# Create a class cal3 that will calculate simple interest. Create
# constructor method which has three parameters .Create calInterest()
# method that will calculate Interest . Create display() method that will
# display Interest.

class Cal3:
    p,r,t=0,0,0  #variable for principle balance, rate of interest & time period(years) as p,r & t respectively
    amount = 0 # final answer
    def __init__(self,a,b,c):
        self.p,self.r,self.t = a,b,c

    def calInterest(self):
        self.amount = self.p*(1 + (self.r*self.t)) # simple interest formula

    def display(self):
        print("Simple Interest is ",self.amount)

a = float(input("Enter balance: "))
b = float(input("Enter rate: "))
c = float(input("Enter time in years: "))
cal = Cal3(a,b,c)
cal.calInterest()
cal.display()