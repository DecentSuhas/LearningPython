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
    while flag >= 0:

        for i in range(len(str)):
            if str[i] == "h":
                count = count + 1
        if count == 1:
            print("Only 1 h is present")
            break
        else:
            flag = -1
            print(count, "h are present")


def strings_slicing():
    s = "Bengaluru"
    first_2_letters = s[:2]
    fifth_letter = s[4]
    multiply_5th_letter = s[4] * 3
    from_4th_letter_to_rest = s[3:]
    last_char = s[-1]
    skip_2nd_letter = s[0:len(s):2]
    revers_string = s[::-1]
    concatenate_sliced_string = s[0:4] + s[4:]
    third_char_starting_Last_till_first_backward = s[-1:0:-3]  # or s[::-3]
    first_and_last_char_approach_1 = s[::-1][-1] + s[len(s) - 1]
    first_and_last_char_approach_2 = s[::-1][::-5]
    first_and_last_char_approach_3 = s[0] + s[-1]
    first_and_last_char_approach_4 = s[0] + s[-1]
    last_and_first_Char = s[::-5]

    print(s[::-1][::-1] == s)  # True
    print(s[:] == s)  # True
    print(s[:] is s)  # True
    print(s[::-1][::-1] is s)  # False

    print(third_char_starting_Last_till_first_backward)


#strings_slicing()
s = "Bengaluru"
if s in "B":
    print(s)


def smallest_largest():
    # Print the smallest and largest word in the given string
    text = "i love my country"
    max_len = 0
    new_text = text.split(" ")
    smallest_word = new_text[0]
    largest_word = ""
    for ele in new_text:
        if len(ele) < len(smallest_word):
            smallest_word = ele
        elif len(ele) > max_len:
            largest_word = ele

    print("Smallest word: ", smallest_word)
    print("Largetst word: ", largest_word)


def palindrome():
    # Ask the user for a string and print out whether this string is a palindrome or not
    text = input("Enter your word: ")
    length = int(len(text))
    is_pal = True
    for i in range(0, int(len(text) / 2)):
        if (text[i] != text[len(text) - i - 1]):
            is_pal = False
    if is_pal:
        print("it is palindrome")
    else:
        print("It is not palindrome")


def print_even():
    # Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    new_list = []
    for num in a:
        if num % 2 == 0:
            new_list.append(num)
    print(new_list)


def reverse_string():
    # Print the words in backwords
    text = "My name is Michele"  #O/P =  "Michele is name My"
    list1 = text.split(" ")
    result = []
    for item in range(len(list1) - 1, -1, -1):
        word = list1[item]
        result.append(word)
    print(" ".join(result))


def check_length():
    # WAP to count the lenght of the string without inbuilt function
    text = "madam"
    num = 0
    count = 0
    try:
        while text[num] != '!':
            count = count + 1
            num = num + 1
    except:
        print(count)


def replace_Charecter():
    '''
    Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char
    Sample String : 'restart'
    Expected Result : 'resta$t'
    '''

    # METHOD 1:
    text = input("Enter your word: ")
    which_char = input("Enter the character you wanna replace: ")
    count = 0
    list1 = list(text)
    for i in range(len(list1)):
        if (list1[i]) == which_char:
            count = count + 1
            if count > 1:
                list1[i] = "$"
    print(" ".join(list1))

    # METHOD 2:
    str1 = "restarted"
    i = 0
    char = " "
    if "e" in str1:
        i = str1.index("e")
        char = str1[i]
    str1 = str1.replace(char, '$')
    str1 = char + str1[1:]
    print(str1)


def find_replace():
    '''
    Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string.
     If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
     Sample String : 'The lyrics is not that poor!' OR 'The lyrics is poor!'
    Expected Result : 'The lyrics is good!' OR    'The lyrics is poor!'
     '''

    text = "Lyric is very poor"
    s_not = text.find("not")
    s_poor = text.find("poor")
    print(s_not)
    print(s_poor)
    if s_poor > s_not > 0 and s_poor > 0:
        text = text.replace(text[s_not:], "good")
    elif s_poor > 0:
        text = text.replace(text[s_poor:], "good")
    print(text)


def replace_first_last_word():
# Write a Python program to change a given string to a newly string where the first and last chars have been exchanged
    text = "abcdef"
    f = text[0]
    l = text[-1]
    print(text[-1] + text[1:-1] + text[0])


def createFromMiddle():
    # Create a string made of the middle three characters
    # CASE : str1 = "JhonDipPeta"
    # SOLUTION: Dip
    str1 = "JhonDipPeta"
    listOfstr = list(str1)
    newList = []
    midValue = int(len(listOfstr) / 2)
    for i in range(midValue - 1, midValue + 2):
        newList.append(listOfstr[i])

    print("".join(newList))


def string_from_f_m_l():
    # Create a new string made of the first, middle, and last characters of each input string
    s1 = "America"
    s2 = "Japan"
    output = "AJrpan"

    f_char = s1[0] + s2[0]
    mid_char = f_char + s1[int(len(s1) / 2)]
    last_char = mid_char + s2[int(len(s2) / 2):]
    print(last_char)


def lowerToUpper():
    # Arrange string characters such that lowercase letters should come first
    str1 = "PyNaTive"  # Output: yaivePNT
    l1 = list(str1)
    temp = ""
    for i in range(0, int(len(l1)) - 1):
        for j in range(i, int(len(l1))):
            if l1[i].isupper():
                temp = l1[i]
                l1[i] = l1[j]
                l1[j] = temp
    print("".join(l1))

def count_chars():
    # Count all letters, digits, and special symbols from a given string
    str1 = "P@#yn26at^&i5ve"
    letter_count = 0
    spl_count = 0
    int_count = 0
    for i in str1:
        if i.isalpha():
            letter_count += 1
        elif i.isnumeric():
            int_count += 1
        else:
            spl_count += 1
    print("No of letters: ", letter_count)
    print("No of special characters: ", spl_count)
    print("No of integers: ", int_count)


def find_occur():
    # Find all occurrences of a substring in a given string by ignoring the case
    str1 = "Welcome to USA usa awesome, isn't it?"
    l1 = str1.split(" ")
    stringToFind = "USA"
    foundinindex = 0
    for i in range(0, len(l1)):
        if l1[i] == stringToFind:
            foundinindex = i

    print(stringToFind + " is found at the index", foundinindex)


def get_avg_num():
    # Calculate the sum and average of the digits present in a string
    str1 = "PYnative29@#8496"
    sum_of_num = 0
    total_digits = 0
    for i in str1:
        if i.isnumeric():
            total_digits += 1
            sum_of_num = sum_of_num + int(i)
    avg = sum_of_num / total_digits
    print(avg)


def remove_spl():
    # Remove special symbols / punctuation from a string
    # Given str1 = "/*Jon is @developer & musician"
    # Expected = "Jon is developer musician"
    str1 = "/*Jon is @developer & musician"
    l1 = []
    for i in str1:
        if i.isalpha():
            l1.append(i)
        elif i.isspace():
            l1.append(i)
    print("".join(l1))


def remove_alpha():
    # Removal all characters from a string except integers
    # Given :'I am 25 years and 10 months old'
    # Output: 2510
    str1 = 'I am 25 years and 10 months old'
    l1 = []
    for i in str1:
        if i.isnumeric():
            l1.append(i)
    print("".join(l1))


def bothalphNum():
    # Find words with both alphabets and numbers
    # Given : "Emma25 is Data scientist50 and AI Expert"
    # output: Emma25
    # scientist50
    str1 = "Emma25 is Data scientist50 and AI Expert"
    str2 = str1.split(" ")
    for i in str2:
        if not i.isalpha():
            print(i)

def replaceSpl():
    # Replace each special symbol with # in the following string
    # Given: '/*Jon is @developer & musician!!'
    # ##Jon is #developer # musician##
    str1 = '/*Jon is @developer & musician!!'
    l1 = []
    for i in str1:
        if not i.isalpha() and not i.isspace():
            replace = "#"
            l1.append(replace)
        elif i.isspace():
            l1.append(i)
        else:
            l1.append(i)
    print("".join(l1))


def string_compress():
    input = 'aabcccccaaa'
    # output = 'a2b1c5a3'
    current_count = 1
    current_char = input[0]
    new_text = []
    for i in range(1, len(input)):
        if input[i] == current_char:
            current_count = current_count + 1
        else:
            new_text.append(current_char)
            new_text.append(str(current_count))
            current_char = input[i]
            current_count = 1

    new_text.append(current_char)
    new_text.append(str(current_count))
    updated_text = ''.join(new_text)
    print(updated_text)