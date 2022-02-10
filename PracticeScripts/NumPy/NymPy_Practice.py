import random

import numpy as np


def basic_1():
    arr = np.array([[1, 2, 3], [3, 6, 5], [7, 8, 33]])
    print(arr.ndim)

    # print the 2nd element of 1st row
    print(arr[0, 1])

    # print the 3rd element of 2nd row
    print((arr[1, 2]))

    # print 33 from the above array
    print((arr[2, 2]))


def addition():
    """ Element-wise addition of 2 numpy arrays """
    a = np.array([1, 2, 3, 4, 5])
    b = np.array([6, 7, 8, 9, 10])
    sum = np.add(a, b)
    print(sum)


def get_index():
    """ Getting the positions (indexes) where elements of 2 numpy arrays match """
    a = np.array([1, 2, 3, 4, 5])
    b = np.array([6, 7, 2, 9, 3])
    for i in range(len(a)):
        com = np.isin(a[i], b)
        if com:
            print("Element", a[i], "of array \'a\' found at the index", np.where(b == a[i]), "of array \'b\'")


def generate_random_ints():
    """ Array Generation of random integers within a specified range """
    arr = np.array([10])
    print("Previous array: ", arr)
    for i in range(0, 10):
        random_num = random.randint(1, 99)
        arr = np.append(arr, random_num)
    print("Updated array: ", arr)


def matrix_multiplication():
    """ Matrix multiplication """
    arr1 = ([1, 2, 3], [4, 5, 6])
    arr2 = ([10, 5, 8], [3, 9, 6])
    print(np.multiply(arr1, arr2))


def test():
    arr = np.array([1, 2, 3, 4, 5, 4, 4])
    x = np.where(arr == 4)
    print(x)
    print(arr)


matrix_multiplication()
