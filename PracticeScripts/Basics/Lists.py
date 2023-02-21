import random


def commonSlicing():
    a = [1, 3, 4]
    b = [1, 4, 3]
    print(a == b)

    a1 = [1, 2, 3, 4, 5]
    print(a1[1:6:2])
    print((a1[-1]))
    print((a1[-3:]))
    print(a1[:-1])
    print((a1[-3:-1]))
    a1[2] = 10
    a1[1:3] = [69, 89]  # Size should be only 2. It wont work if you give a1[1:3:4]
    a1[-1] = 38
    a1.append(100)
    print(a1)


def built_in_func():
    list1 = [99, 2, 4, 200, 6, 987, 8, 90]
    str2 = 'Jonathan'
    print(max(list1))
    print(min(list1))
    print(list(str2))


def printOdds():
    """ Use a loop to display elements from a given list present at odd index positions """
    list_a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    for i in range(1, len(list_a)):
        if i % 2 != 0:
            print(list_a[i])


def remove_dups():
    """ Write the program to remove the duplicate element of the list. """
    list_a = ['Raju', 'Rana', 'Shinu', 'Raju', 'Mona', 'Shyama', 'Shinu', 'Shyama']
    for i in range(0, len(list_a)):
        str1 = list_a[i]
        for k in range(0, i):
            s = list_a[k]
            if list_a[k] == str1:
                print("Duplicate found : ", list_a[k])
                break


def print_sum_of_list():
    """ Write a program to find the sum of the element in the list. """
    sum1 = 0
    list_a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    for i in list_a:
        sum1 = sum1 + i
    print(sum1)


def find_common_element():
    """ Write the program to find the lists consist of at least one common element."""

    list1 = ['India', 'USA', 'Sri Lanka', 'Poland', 'Russia']
    list2 = ['India', 'Serbia', 'Chile', 'Romania', 'Poland']
    for i in range(len(list1)):
        str1 = list1[i]
        for k in range(0, len(list2)):
            str2 = list2[k]
            if str2 == str1:
                print("Common element found: ", str2)


def count_unique_value():
    """ Python Program to count unique values inside a list  -- Needs fix """
    list1 = [2, 2, 2, 2, 4, 2, 2, 2]


def list_product():
    """ Python – List product   -- Needs fix """
    prod = 0
    list1 = [1, 2, 3, 4]
    for i in range(0, len(list1)):
        num1 = list1[i]
        print("Num1: ", num1)
        for k in range(0, i):
            num2 = list1[k]
            print("Num2: ", num2)
            prod = num1 * num2
            # print(prod)


def list_in_range():
    """ Python – Test if List contains elements in Range - Guessed logic """
    list1 = ['a', 'b', 'c', 'd']
    for i in range(len(list1)):
        text = input("Enter the letter: ")
        if text == list1[i]:
            print("Element is found at the index ", i)
            print("Searched element is: ", text, " and element in the list is: ", list1[i])


def biggest_num():
    """ Python - Find biggest number """
    list1 = [99, 2, 4, 200, 6, 987, 8, 90]
    # You can use max function as well . max(list1)
    max1 = 0
    for i in range(len(list1)):
        for k in range(len(list1)):
            if list1[k] > list1[i]:
                max1 = list1[k]
    print(max1)


def possible_combination():  # Incorrect code
    list1 = [2, 9, 8]
    combination_count = 0
    for i in range(0, len(list1)):
        element_1 = str(list1[i])
        for k in range(len(list1)):
            element_1 = element_1 + str(list1[k])
            print(element_1)


def remove_duplicates():
    """ Find the duplicate from 2 lists and if found remove it. """
    list1 = ['cat', 'dog', 'cow', 'Horse']
    list2 = ['Parrot', 'Pigeon', 'Eagle', 'cow']
    final_list = []
    for i in range(len(list1)):
        final_list.append(list1[i])
        for k in range(len(list2)):
            if list1[i] == list2[k]:
                list2.remove(list2[k])
    for j in range(len(list2)):
        final_list.append(list2[j])
    print(final_list)

def remove_dubplicates_sol2():
    list1 = ['cat', 'dog', 'cow', 'Horse']
    list2 = ['Parrot', 'Pigeon', 'Eagle', 'cow']
    list3 = []
    for i in list1:
        if i not in list3:
            list3.append(i)
    for i in list2:
        if i not in list3:
            list3.append(i)
    print(list3)

def count_uniques():
    """ Python Program to count unique values inside a list """
    list1 = [2, 3, 4, 5, 6, 6, 7, 9, 9]
    print(len(list1))
    list2 = list(set(list1))
    print(len(list2))


def product_excluding_dupes():
    """ Python – List product excluding duplicates """
    list1 = [2, 3, 4, 5, 6, 6, 7, 9, 9]
    prod = 1
    unique_list = list(set(list1))
    print(unique_list)
    for i in range(len(unique_list)):
        prod = prod * unique_list[i]
    print(prod)


def extract_repeats():
    """ Python – Extract elements with Frequency greater than K """
    '''
    Input : test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8], K = 3
    Output : [4, 3]
    Explanation : Both elements occur 4 times.
    '''
    list1 = [3, 3, 3, 4, 5, 6, 6, 6, 7, 9, 9, 9, 10, 10, 10]
    k_value = 2
    print("K value is: ", k_value)
    count = 0
    for i in range(len(list1)):
        num1 = list1[i]
        for k in range(0, i):
            num2 = list1[k]
            if num1 == num2:
                count = count + 1
                if count > k_value:
                    print("List item", list1[i], "is found with frequency greater than K")
                    count = 0
                    break


def uniquess():
    """ Python program to get all unique combinations of two Lists """


def removeOccurrence(ele):
    """ Python program to remove all the occurrences of an element from a list """
    list1 = [2,3,4,5,4,6,7,5,4,9,10,4]
    count = 0
    for i in list1:
        if i == ele:
            count = count+1
            if count >1:
                list1.remove(i)
    print(list1)

remove_duplicates()