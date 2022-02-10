# Concatenate all keys which have similar values
def print_SimilarKeys():
    names = {'Name1': 'Tony', 'Name2': 'Rony', 'Name3': 'Peter', 'Name4': 'Joy', 'Name5': 'Tony', 'Name6': 'Rony'}
    str1 = " "
    for i in names.items():
        str1 = i
        print(str1)

    print(str1)


def basics():
    names = {'Name1': 'Raju', 'Name2': 2, 'Name3': 3, 'Name4': 4, 'Name5': 5, 'Name6': 6}
    age = {'peter':35,'sana':24, 'Sumitra':45}
    print(str(names))
    print(dict(names))
    print(names.fromkeys('Name1')) # ---> {'N': None, 'a': None, 'm': None, 'e': None, '1': None} Here it creates a new dict from the iterable with value equal to value
    print(names.get('Name1'))  # --> Raju
    print(names.items())
    (names.setdefault('Name7')) # --> Name7:None  It is used to set the key to the default value if the key is not specified in the dictionary
    print(names)
    names.update(age)
    print(names)
    names.popitem()  # Removes the last item of the list
    print(names)
    names.pop('Name1') # Removes the specified item of the list
    print(names)

print_SimilarKeys()