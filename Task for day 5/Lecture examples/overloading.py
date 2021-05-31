class Demo:
    def sum(self,a,b):
        ans = a+b
        print("sum is ",ans)

    def sum(self,a,b,c):
        ans = a+b+c
        print("sum is ",ans)

d = Demo()
d.sum(10,20)
d.sum(10,20,30)

#python does not support overloading that's why here instead of output ,
#it throws traceback