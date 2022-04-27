class Employee:
    """ Class without a constructor """

    def details(self, emp_name, emp_id, emp_dept):
        print(" ID:", emp_id, '\n', "Name:", emp_name, '\n', "Department:", emp_dept)


test = Employee()


# test.details(emp_name='Rahul Bocha', emp_id=89878, emp_dept="IT Services")


class School:
    """ Class with default constructor """

    def __init__(self):
        print("Printing the default constructor")

    def details(self, roll_no, name, section):
        print("Roll no:", roll_no, "Name:", name, "Cass:", section)


# test1 = School()


# test1.details(12334, "Raju", "C")


class Vehicles:
    """ With parameterised constructor
    When parameterised constructor is defined then it is mandatory to provide the values while creating the object
    of the respective class
    """

    def __init__(self, model, year, manufacturer):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer

    def printDetails(self):
        print("Model:", self.model, "Year:", self.year, "Manufacturer:", self.manufacturer)


# This works
test2 = Vehicles("Harrier", 2020, "Tata")


# test2.printDetails()

# This doesnt work  TypeError: __init__() missing 3 required positional arguments: 'model', 'year', and 'manufacturer'
# test3 = Vehicles()
# test3.model = "Compass"
# test3.year = 2021
# test3.manufacturer = "JEEP"
# test3.printDetails()


class Pets:
    """ It is possible to define more than 1 constructor in the class
    When 2 default constructor is defined then the last constructor is executed because constructor overriding is
    not allowed in python.
    """

    def __init__(self):
        print("This is first constructor")

    def __init__(self):
        print("This is second constructor")


# s1 = Pets()


class Birds:
    """ It is possible to define more than 1 constructor in the class
    When 2 default constructor is defined then the last constructor is executed.
    """

    def __init__(self, animal, age):
        print("Animal:", animal, "Age:", age)

    def __init__(self, animal, age):
        print("Bird:", animal, "Age:", age)


# Birds("Parrot",1)


class Pupil:
    """ For some of the attributes"""

    def __init__(self, name, ids, age):
        self.name = name
        self.ids = ids
        self.age = age


# pup = Pupil("Renita", 2222, 21)  # prints the attribute name of the object pup
# print(getattr(pup, 'name'))
# setattr(pup, "age", 23)
# print(getattr(pup, 'age'))
# print(hasattr(pup, 'ids'))  # prints true if the student contains the attribute with name ids
# delattr(pup, 'age')  # deletes the attribute age


class Vehicles:
    """ Write a Python program to create a Vehicle class with max_speed and mileage instance attributes. """

    def __init__(self, mileage, max_speed):
        self.mileage = mileage
        self.max_speed = max_speed

    def printVehicleCapacity(self):
        print("Max_speed: ", self.max_speed, "Mileage: ", self.mileage)


# test = Vehicles(17,160)
# test.printVehicleCapacity()
# print(test.__doc__)


class Vehicle:
    name = ""
    color = ""
    price = ""
    type = ""

    def car1(self, name, color, price, type):
        print(f"Car1 details: , {name}, {color}, {price}, {type}")

    def car2(self, name, color, price, type):
        print(f"Car2 details: , {name}, {color}, {price}, {type}")


test = Vehicle()
test.car1("Fer","Red","60000","Convertible")
test.car2("Jump","Blue","100000","Van")