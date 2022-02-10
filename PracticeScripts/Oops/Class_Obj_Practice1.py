class Bank:
    roi = 0

    # def __init__(self):
    #     roi = 8
    #     print("Bank roi", roi)

    def calculation(self):
        total = (100*Bank.roi)/100
        print("Total:",total)

test = Bank()
test.calculation()