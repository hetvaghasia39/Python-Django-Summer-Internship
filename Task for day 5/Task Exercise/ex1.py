class Cal1:
    n1,n2,n3=0,0,0
    def setdata(self,a,b,c):
        print("3 numberes stored in setdata() method")
        self.n1,self.n2,self.n3=a,b,c
    
    def display(self):
        ans = (self.n1 + self.n2 + self.n3)
        print("sum is ",ans)

cal = Cal1()
cal.setdata(10,20,30)
cal.display()