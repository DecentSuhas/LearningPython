from abc import ABC,abstractmethod
class Car(ABC):
    def mileage(self):
        pass
    def demo(self):
        print("hello iam from abstract class")

class Tesla(Car):
    def mileage(self):
        print("The mileage is 30Kmph")
class Suzuki(Car):
    def mileage(self):
        print("The mileage is 25kmph")
class Duster(Car):
    def mileage(self):
        print("the mileage is 24kmph")
class Renault(Car):
    print("The mileage is 27kmph")


t = Tesla()
t.mileage()
t.demo()

r = Renault()
r.mileage()
r.demo()

s = Suzuki()
s.mileage()

d = Duster()
d.mileage()
