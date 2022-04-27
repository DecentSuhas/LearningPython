import json


# Write a Python program to convert JSON data to Python object.
import operator


def json_obj():
    data = '{ "Name":"David", "Class":"I", "Age":6 }'
    py_obj = json.loads(data)  # --> Saves in dict format. So perform all dict operations
    print(type(py_obj))
    print(py_obj['Name'])
    print(py_obj['Class'])


# Write a Python script to sort (ascending and descending) a dictionary by value
def dict_sort():
    # Approach 1
    d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
    # print(sorted(d.items()))
    # print(sorted(d.keys()))
    # print(sorted(d.values()))

    # Approach 2   -->Incomplete.
    min1 = min(d.keys())
    max1 = max(d.keys())
    list1 = []
    for i in d.items():
        if i.key>min1 and i.key<max1:
            list1.append(d[i])
            min1 = i.key
    print(list1)
dict_sort()