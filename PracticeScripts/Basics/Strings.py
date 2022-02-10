# Print the paragraph such that first letter after every full stop is capitalized
def capitalize_paragraph():
    str = "it is a dummy text. to capitalize the first letter of the each letter after each full stop. lets see"
    sentence = str.split('.')
    for i in sentence:
        print(i.strip().capitalize() + '. ', end='')


# WAP to capitalize entire string
def capitalize_entire_String():
    str = input("Enter the string: ")
    updated_string = str.upper()
    print(updated_string)


# change to first letter capital list python
def first_capital_list():
    list1 = ['python', 'google', 'go', 'java']
    for i in range(len(list1)):
        str1 = list1[i].capitalize()
        list1[i] = str1
    print(list1)


# capitalize first letter of each word
def first_letter_each_word():
    str1 = "this is a sample text"
    str2 = str1.split(' ')
    list1 = []
    ss = ' '
    for i in str2:
        updated_str = i.strip().capitalize()
        ss = ss + updated_str + ' '
    print(ss)


# Capitalize only the first letter of first word
def first_letter_word():
    str = "parenting of the millenium"
    print(str.capitalize())


# Count only the capital letters in a string
def count_of_capitals():
    str1 = "Testing this sentense. Monday is first day of the week. Capital, Capital"
    count = 0
    cap_letters = []
    for i in str1:
        if i.isupper():
            count = count + 1
            cap_letters.append(i)

    print("Total count of capital letters are: ", count)
    print(cap_letters)


# check if string is palindrome
def verify_palindrome():
    str1 = "malayalam"
    start = 0
    mid = (len(str1) - 1) // 2
    last = (len(str1) - 1)


# Print the string in reverse
def reverse_string():
    str1 = "testing"


def simpleCode():
    str_1 = 'MyBLog'
    a = ' '
    for i in range(len(str_1)):
        print(i * str_1[i])


def slicing():
    s = 'Bloggings'
    print(s[0:])  # Bloggings
    print(s[0:4])  # Blog
    print(s[:4])  # Blog
    print(s[1:5])  # logg
    print(s[1:])  # loggings
    print(s[len(s) - 1])  # s
    print(s[len(s) - 2:])  # gs
    print(s[len(s) - 4:])  # ings


def count():
    str = "holauhhhja"
    count = 0
    flag = 0
    while flag>=0:

        for i in range(len(str)):
            if str[i] == "h":
                count = count + 1
        if count == 1:
            print("Only 1 h is present")
            break
        else:
            flag = -1
            print(count, "h are present")
count()