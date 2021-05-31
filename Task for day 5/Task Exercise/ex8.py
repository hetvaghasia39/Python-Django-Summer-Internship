# Write a program with use of inheritance: Define a class publisher that
# stores the name of the title. Derive two classes book and tape, which
# inherit publisher. Book class contains member data called page no and
# tape class contain time for playing. Define functions in the appropriate
# classes to get and print the details. 

class Publisher:
    name = "Akash Publication"
    def display(self):
        print("Name: ",self.name)

class Book(Publisher):
    pageNo = "500"
    def display1(self):
        print("pageNo: ",self.pageNo)

class Tape(Publisher):
    time = 10
    def display2(self):
        print("Time: ",self.time)

b = Book()
t = Tape()
b.display()
b.display1()
t.display2()