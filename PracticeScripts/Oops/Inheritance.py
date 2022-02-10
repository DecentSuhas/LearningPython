class Banking:
    roi = 8

class SBI(Banking):

    def __init__(self, principle):
        self.principle = principle

    def values(self):
        total = (self.principle*Banking.roi)/100
        print(total)


s = SBI(200)
s.values()

################   muitiple inheritance   #################
print("muitiple-inheritance")
class Calculation1:
    def Summation(self,a,b):
        return a+b;
class Calculation2:
    def Multiplication(self,a,b):
        return a*b;
class Derived(Calculation1,Calculation2):
    def Divide(self,a,b):
        return a/b;
d = Derived()
print(d.Summation(10,20))
print(d.Multiplication(10,20))
print(d.Divide(10,20))

#issubclass
print("issubclass")
print(issubclass(Derived,Calculation2))
print(issubclass(Calculation1,Calculation2))

#isinstance (obj, class) method
print("isinstance (obj, class) method")
print(isinstance(d,Calculation2))




##################  multi-level  ######################
print("multi-level")

class Animal:
    def speak(self):
        print("Animal Speaking")
#The child class Dog inherits the base class Animal
class Dog(Animal):
    def bark(self):
        print("dog barking")
#The child class Dogchild inherits another child class Dog
class DogChild(Dog):
    def eat(self):
        print("Eating bread...")
d = DogChild()
d.bark()
d.speak()
d.eat()

class Vehicle_1:
    """ Create a Bus object that will inherit all of the variables and methods of the parent Vehicle class and display it."""

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Buss(Vehicle_1):

    def printDetails(self):
        print("Vehicle name:",self.name, "Mileage:",self.mileage, "Max_speed:",self.max_speed)

school_buss = Buss("Volvo", 240, 22)
print(school_buss.printDetails())


class Vehicle_2:
    """ddd"""

    def __init__(self,name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of {self.name} is {self.capacity} passengers"

class Bus_2(Vehicle_2):
    def seating_capacity(self, capacity = 10):
        return super().seating_capacity(capacity=10)

collage_bus = Bus_2("Volvo",240,12)
print(collage_bus.seating_capacity())