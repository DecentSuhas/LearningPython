class Bank:
    roi = 0

    # def __init__(self):
    #     roi = 8
    #     print("Bank roi", roi)

    def calculation(self):
        total = (100 * Bank.roi) / 100
        print("Total:", total)


test = Bank()
test.calculation()


class Modifiers:
    __name = None
    __Age = None
    __country = None

    def __init__(self, name, age, country):
        self.__name = name
        self.__age = age
        self.__country = country

    def __display_privatemember(self):
        print(self.__name)
        print(self.__age)
        print(self.__country)

    def call_display_func(self):
        self.__display_privatemember()


object = Modifiers("Tomy Shelby", 40, "England")
object.call_display_func()