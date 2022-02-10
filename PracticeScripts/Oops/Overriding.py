class Animal:
    def speak(self):
        print("speaking")
class Dog(Animal):
    def speak(self):
        print("Barking")
d = Dog()
d.speak()


class Bank:
    def getroi(self):
        return 10;


class SBI(Bank):
    def getroi(self):
        return 7;


class ICICI(Bank):
    def getroi(self):
        return 8;


b1 = Bank()
b2 = SBI()
b3 = ICICI()
print("Bank Rate of interest:", b1.getroi());
print("SBI Rate of interest:", b2.getroi());
print("ICICI Rate of interest:", b3.getroi());