"""

Some key points about tuple
1. Tuples are ordered and the order will not change
2. Tuples are unchangeble. Meaning you can not add, remove items
3. Tuples allow duplicates
4. Tuple itmes are indexed [0] ... [n]
5. You can create tuple with 1 item but comma is imp. CORRECT: fruites = ("apple",)  INCORRECT: fruites = ("apple")
6. Tuple accepts different datatypes.



"""




def find_index():
    tuple1 = ('1', '2', '3')
    print(tuple1)
    tuple1 = tuple(input("enter the string: "))
    count = 0
    for i in tuple1:
        print("tuple1[%d] = %s" % (count, i))
        count = +1


def tuple_slicing():
    tuples = (1, 2, 3, 4, 5, 6, 7)
    print(tuples[1:])
    print(tuples[1:4])
    print(tuples[:4])
    print(tuples[-1])
    print(tuples[-4:-1])
    print(tuples[-4:])
    print(tuples[:-1])
    print("&&&&&&")
    print(tuples)


def tuple_compare():
    tuple1 = ('h', 'e', 'l', 'l', 'o')
    tuple2 = ('h', 'e', 'l', 'l', 'o')
    tuple3 = ('w', 'o', 'r', 'd')
    if tuple1 == tuple2:
        print("Tuple 1 is same as Tuple 2")
    elif tuple1 == tuple3:
        print("Tuple 1 is same as Tuple 3")
    elif tuple2 == tuple3:
        print("Tuple 2 is same as Tuple 3")
    else:
        print("None of them are same")


def print_evens():
    tuple1 = (1, 2, 3, 4, 5, 6)
    for i in range(len(tuple1)):
        if i % 2 == 0:
            print("Even number is found ", i)


def built_ins():
    tuple1 = (3, 7, 1, 28, 91)
    str1 = 'Jonathan'
    print(max(tuple1))
    print(min(tuple1))
    # print(tuple(str1))
    tuple_a = ('h', 'e', 'l', 'l', 'o')
    tuple_b = ('w', 'o', 'r', 'l', 'd')
    tuple_c = tuple_a + tuple_b
    tuple_d = tuple_a * 2
    print(tuple_d)


# Python program to find tuples which have all elements divisible by K from a list of tuples
def find_divisible_element():
    ele = int(input("Enter the number K: "))
    tuple1 = (1, 2, 3, 4, 5, 6, 7, 8)
    for i in tuple1:
        if i % ele == 0:
            print(i, "is divisible by ", ele)


#
def find_positive_elements():
    """ Python program to find Tuples with positive elements in List of tuples """
    tuple1 = (2, -4, -3, 9, -10, -7, 99, -100)
    positive_count = 0
    negative_count = 0
    for i in tuple1:
        if i > 0:
            print(i, "is positive element")
            positive_count = positive_count + 1
        else:
            print(i, "is negative element")
            negative_count = negative_count + 1
    print("Total positive elements count is : ", positive_count)
    print("Total negative elements count is : ", negative_count)


def list_of_tuple():
    """ Python – Count tuples occurrence in list of tuples """
    list1 = [(1, 2, 3), (3, 4, 5), (5, 6, 7), (7, 8, 9), (1, 2, 3), (7, 8, 9)]
    count = 0
    for i in range(len(list1)):
        value1 = list1[i]
        for k in range(0, i):
            if list1[k] == value1:
                count = count + 1
                break
    print("Total count of duplicate tuple is :", count)


def remove_duplicates_tuple():
    """Python – Removing duplicates from tuple"""
    tuple1 = (1, 2, 3, 4, 4, 5, 6, 7, 4)
    list1 = list(tuple1)
    count = 0
    for i in range(0, len(list1)):
        value1 = list1[i]
        for k in range(0, i):
            value2 = list1[k]
            if value2 == value1:
                count = count + 1
                if count > 1:
                    list1.remove(value2)
    print(tuple(list1))


def sort_alphabetically():
    """ Python program to sort a list of tuples alphabetically """
    tuple1 = ('a', 'd', 'b', 'f', 'e', 'x', 'c')
    list1 = list(tuple1)
    list1.sort()
    tuple1 = tuple(list1)
    print(tuple1)


tuple_compare()
