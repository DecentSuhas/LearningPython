# Use a loop to display elements from a given list present at odd index positions
def printOdds():
    list_a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    for i in range(1, len(list_a)):
        if i % 2 != 0:
            print(list_a[i])


# Write the program to print the duplicate element of the list.
def remove_dups():
    list_a = ['Raju', 'Rana', 'Shinu', 'Raju', 'Mona', 'Shyama', 'Shinu', 'Shyama']
    for i in range(0, len(list_a)):
        str1 = list_a[i]
        for k in range(0, i):
            if list_a[k] == str1:
                print("Duplicate found : ", list_a[k])
                break


# Write a program to find the sum of the element in the list.
def print_sum_of_list():
    sum1 = 0
    list_a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    for i in list_a:
        sum1 = sum1 + i
    print(sum1)


# Write the program to find the lists consist of at least one common element.
def find_common_element():
    list1 = ['India', 'USA', 'Sri Lanka', 'Poland', 'Russia']
    list2 = ['India', 'Serbia', 'Chile', 'Romania', 'Poland']
    for i in range(len(list1)):
        str1 = list1[i]
        for k in range(0, len(list2)):
            str2 = list2[k]
            if str2 == str1:
                print("Common element found: ", str2)


# #############################################################################


# Python program to find tuples which have all elements divisible by K from a list of tuples
def find_divisible_element():
    ele = int(input("Enter the number K: "))
    tuple1 = (1, 2, 3, 4, 5, 6, 7, 8)
    for i in tuple1:
        if i % ele == 0:
            print(i, "is divisible by ", ele)

# Python program to find Tuples with positive elements in List of tuples
def find_positive_elements():
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


def extract_elements_greater_frequency():
    """ Python – Extract elements with Frequency greater than K """
    list1 = [3, 3, 3, 4, 5, 6, 6, 6, 7, 9, 9, 9]
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
                    print("Value ", list1[i], "found with frequency greater than K")
                    count = 0
                    break