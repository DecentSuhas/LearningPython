def printEven():
    i = 0
    while i < 10:
        if i % 2 == 0:
            print("\'i\'value is even ", i)
        i = i + 1



def printSquares():
    """ Write a program to print first 10 integers and their squares using while loop """
    i = 1
    print("Printing squares")
    print("Numbers", '\t', 'Squares')
    while i <= 10:
        sqr = i * i
        print(i, '\t\t\t', sqr)
        # print(i, " X ", i, " = ", sqr)
        i = i + 1

def test():
    check = True
    while check:
        print("false")
        value = input("Enter string: ")
        if value=="hi":
            check = False

test()
