import random




def printOdds():  #Complexity : O(1 + 3n) = O(n)
    """ Use a loop to display elements from a given list present at odd index positions """
    list_a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']  #O(1)
    for i in range(1, len(list_a)): #O(n)
        if i % 2 != 0: #O(n)
            print(list_a[i]) #O(n)


def remove_dups(): #Complexity :
    """ Write the program to remove the duplicate element of the list. """
    list_names = ['Raju', 'Rana', 'Shinu', 'Raju', 'Mona', 'Shyama', 'Shinu', 'Shyama']  #O(1)
    new_list = []
    for name in list_names:
        if name not in new_list:
            new_list.append(name)
    print(new_list)


def print_sum_of_list():  # Complextity: O(3 + 2n) == O(n)
    """ Write a program to find the sum of the element in the list. """
    sum1 = 0  #O(1)
    list_a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]  #O(1)
    for i in list_a: #O(n)
        sum1 = sum1 + i #O(n)
    print(sum1) #O(1)


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




def list_in_range():
    """ Python – Test if List contains elements in Range - Guessed logic """
    list1 = ['a', 'b', 'c', 'd']  #O(1)
    for i in range(len(list1)): #O(n)
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


def count_uniques():
    """ Python Program to count unique values inside a list """
    list1 = [2, 3, 4, 5, 6, 6, 7, 9, 9]
    print(len(list1))
    list2 = list(set(list1))
    print(len(list2))


def product_excluding_dupes():
    """ Python – List product excluding duplicates """
    list1 = [2, 3, 3, 4, 5]
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


def ascending_order():
    list1 = [99, 2, 4, 200, 6, 987, 8, 90]
    temp = 0

    for i in range(0, len(list1)):
        for j in range(i, len(list1)):
            if (list1[j] < list1[i]):
                temp = list1[j]
                list1[j] = list1[i]
                list1[i] = temp
    print(list1)


def descending_order():
    list1 = [99, 2, 4, 200, 6, 987, 8, 90]
    temp = 0

    for i in range(0, len(list1)):
        for j in range(i, len(list1)):
            if (list1[i] < list1[j]):
                temp = list1[j]
                list1[j] = list1[i]
                list1[i] = temp
    print(list1)


def largest():
    list1 = [99, 2, 4, 200, 6, 987, 8, 90]
    max = 0
    for i in list1:
        if(i>max):
            max=i
    print(max)


def print_less_than_5():
    # write a program that prints out all the elements of the list that are less than 5.
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    new_list = []
    for num in a:
        if num < 5:
            new_list.append(num)
    print(new_list)