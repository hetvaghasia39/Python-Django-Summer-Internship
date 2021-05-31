# Consider an employee class, which contains fields such as name and
# designation. And a subclass, which contains a field salary. Write a
# program for inheriting this relation.

class Employee:
    name = "Het"
    designation = "Developer"

class EmployeeField(Employee):
    salary = 30000

emp = EmployeeField
print("Employee details are \nName: ",emp.name,"\nDesignation: ",emp.designation,"\nsalary: ",emp.salary)