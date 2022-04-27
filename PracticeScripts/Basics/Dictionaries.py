# Concatenate all keys which have similar values
import collections


def print_SimilarKeys():
    names = {'Name1': 'Tony', 'Name2': 'Rony', 'Name3': 'Peter', 'Name4': 'Joy', 'Name5': 'Tony', 'Name6': 'Rony'}
    str1 = " "
    for i in names.items():
        str1 = i
        print(str1)

    print(str1)


def basics():
    names = {'Name1': 'Raju', 'Name2': 2, 'Name3': 3, 'Name4': 4, 'Name5': 5, 'Name6': 6}
    age = {'peter': 35, 'sana': 24, 'Sumitra': 45}
    print(str(names))
    print(dict(names))
    print(names.fromkeys(
        'Name1'))  # ---> {'N': None, 'a': None, 'm': None, 'e': None, '1': None} Here it creates a new dict from the iterable with value equal to value
    print(names.get('Name1'))  # --> Raju
    print(names.items())
    (names.setdefault(
        'Name7'))  # --> Name7:None  It is used to set the key to the default value if the key is not specified in the dictionary
    print(names)
    names.update(age)
    print(names)
    names.popitem()  # Removes the last item of the dict
    print(names)
    names.pop('Name1')  # Removes the specified item of the dict
    print(names)


def convert_list_to_dict():
    """
    Write a Python program to convert them into a dictionary in a way that item from list1 is the key and item from list2 is the value
    :return:
    """
    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10, 20, 30]

    dict1 = dict(zip(keys, values))
    print(dict1)


def two_dicts_to_one():
    """
    Merge two Python dictionaries into one
    :return:
    """
    dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
    dict1.update(dict2)

    print(dict1)


def defaults():
    dict1 = collections.defaultdict(int)
    print(dict1)


def create_dict():
    # Option 1:
    new_dict = dict()
    # Option 2:
    new_dict = {}


def get_value_by_key():
    dict1 = {'a': 20.5, 'b': 3.03, 'c': 23.22, 'd': 33.12}
    # Option 1:
    print(dict1['a'])
    # Option 2:
    print(dict1.get('a'))


def add_key_value():
    dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

    # Option 1:
    dict1['Forty'] = 40
    print(dict1)

    # Option 2:
    dict0 = {'Fifty': 50}
    dict1.update(dict0)   # Also it is concatination
    print(dict1)

    # Option 3:
    dict1.update({'Sixy': 60})
    print(dict1)


def iterate_over():
    dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    for key in dict1.keys():
        print(key)

    for value in dict1.values():
        print(value)

    for item in dict1.items():
        print(item)

    for key, value in dict1.items():
        print(key, value)


def remove():
    dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    del dict1['Ten']  # Removes the specified item of the dict
    dict1.pop('Twenty')  # Removes the specified item of the dict
    dict1.popitem()  # Removes last item
    del dict1  # Deletes the whole dictionary


def sort_by_key():
    dict1 = {20: 'Twenty', 10: 'Ten', 30: 'Thirty'}
    sorted(dict1)  # This is useless
    print(dict1)

    for value in sorted(dict1):
        print(value)


def getmaxAndMin():
    my_dict = {'x': 500, 'y': 5874, 'z': 560}
    print(max(my_dict.values()))  # >> 5874
    print(max(my_dict.keys()))    # >> z
    print(min(my_dict.values()))  # >> 500
    print(min(my_dict.keys()))  # >> x


def isDictHasKey():
    fruites = {'Apple':10, 'Mango':5, 'Grapes':5}
    if 'Apple' in fruites:
        print("Apple is present")
    else:
        print("Not present")

    if 'Guava' in fruites:
        print("Guava is present")
    else:
        print("Guava is not present")


