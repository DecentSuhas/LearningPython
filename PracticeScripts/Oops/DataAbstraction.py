class demo:
    a = 10
    def display(self):
        print("this is demo ", demo.a)

d = demo()
d.display()
print(d.a)


class Employee:
    __count = 0
    def __init__(self):
        Employee.__count = Employee.__count + 1
    def display(self):
        print("the no of employees",Employee.__count)
emp = Employee()
emp2 = Employee()
try:
    print(emp.__count)
finally:
    emp.display()

