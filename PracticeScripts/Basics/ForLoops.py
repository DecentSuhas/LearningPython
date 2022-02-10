list1 = ['1', '2', '3', '4', '5']


# for i in range(len(list1)-1,-1,-1):
#     print(list1[i])


def loopExhausted():
    for i in range(10 - 1, 10, -1):
        print(i)

    for i in range(0, 10):
        print(i)
    else:
        print("Loop is exhausted")


def sumSeries():
    n = 5
    start = 3,
    sum_seq = 0
    for i in range(0, n):
        print(start, end="+")
        sum_seq += start
        start = start * 10 + 2
    print("\n Sum of above serires is : ", sum_seq)


# list2 = ['a','b,','c','d','e','f']
# for i in range(0,len(list2),2):
#     print(list2[i])


def findNumLocation_1():
    num = int(input("enter the string: "))
    list10 = [10, 20, 30, 40, 50]
    for i in range(len(list10)):
        if list10[i] == num:
            print("Number is ", num)
            print("Number found at index: ", i)
            break
    else:
        print("Number is not found")


def numLocation_2():
    list2 = [1, 2, 3, 4]
    count = 1;
    for i in list2:
        if i == 4:
            print("item matched")
            count = count + 1;
            break
    print("found at", count, "location");



def print10s():
    """ Write for loop statement to print the following series: 10, 20, 30 … … 300 """
    i = 1
    while i <= 30:
        prod = i * 10
        print(prod)
        i = i + 1


def print7s():
    """ Write a while loop statement to print the following series:  105, 98, 91 ………7. """
    i = 105
    while i >= 7:
        print(i)
        i = i - 7


def naturalNum_reverse():
    """ Write a program to print first 10 natural number in reverse order using while loop. """
    i = 10
    while i >= 1:
        print(i)
        i = i - 1


def sumOfNaturals():
    """ Write a program to print sum of first 10 Natural numbers. """
    i = 1
    sum1 = 0
    while i <= 10:
        sum1 = sum1 + i
        i = i + 1
    print("Sum is : ", sum1)

def test():
    count = 0
    for i in range(3):
        print("hi")
        count = count+i
        if count>3:
            print("Esceeded limint")

test()