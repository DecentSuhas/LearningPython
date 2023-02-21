'''
 Set_1
 Set_2
 Union() :        It compares 2 sets and removes 1 duplicate of common elements and returns the unique
 intersection() : It compares 2 sets and returns only the common element(s)
 intersection_update() : It compares set_1 with set_2 and set_3 for common elements
 Subtract  :      It removes common elements depending on first mentioned set.
 symmetric_difference() : It removes common elements depending on first mentioned set.
 isdisjoint() :   It compares 2 sets and returns TRUE if no common elements are found
 isSubset() :     It checks if the set 'A'(all elements) are present in set 'B' and returns TRUE. (position of elements doesnt matter)
 isSuperset() :   It checks if the set 'B'(all elements) are present in set 'A' and returns TRUE
 difference_update() : It checks the set B as per elements present in set A. Removes all common elements and retuns only the unique elements of set A.

'''


def basic():
    set1 = set()
    months = set(['Rome', 'Italy'])
    months.add('Paris')
    months.update(['India'])
    months.discard('Rome')
    months.remove('Italy')
    months.pop()
    months.clear()


def union_of_sets():
    set1 = {'a', 'b', 'c'}
    set2 = {'b', 'd', 'e', 'f'}
    set3 = set1 | set2
    print(set3)
    set4 = set1.union(set2)
    print(set4)


def intersection_of_sets():
    set1 = {'ball', 'bat', 'wicket', 'helmet'}
    set2 = {'pad', 'gloves', 'ball', 'helmet'}
    set3 = set1 & set2
    print(set3)
    set4 = set1.intersection(set2)
    print((set4))
    # Except common elements rest other elements are removed
    # Output: {'ball'}


def intersection_update_of_sets():
    a = {"Bull", "Cat", "dog", "Rat"}
    b = {"Cat", "Cow", "Goat", "Rat"}
    c = {"Bird", "Cat", "Horse", "Rat"}
    a.intersection_update(b, c)
    print(a)
    # Except common element, remaining elements will be removed from the set
    # Output: {'Rat', 'Cat'}


def subtraction_of_sets():
    da1 = {"Mon", "Tue", "Wed", "Fri"}
    da2 = {"Mon", "Tue", "Sun", "Thurs"}
    print(da1 - da2)  # Output: {'Fri', 'Wed'}
    print(da2 - da1)  # Output: {'Thurs', 'Sun'}
    # Symmetric difference
    a = {1, 2, 3, 4, 5, 6}
    b = {1, 2, 9, 8, 10}
    c = a ^ b
    print(c)
    print(a.symmetric_difference(b))
    # Output 2: {3, 4, 5, 6, 8, 9, 10}
    # Common elements are removed depending on first mentioned set.


def verify_isdisjoint():
    # Return True if two sets have a null intersection.
    set1 = {'ball', 'bat', 'wicket'}
    set2 = {'pad', 'gloves', 'shoe'}
    print("isdisjoint: ", set1.isdisjoint(set2))
    set1 = {'ball', 'bat', 'wicket'}
    set2 = {'pad', 'gloves', 'ball'}
    print("isdisjoint: ", set1.isdisjoint(set2))


def verify_isSubset():
    # Report whether another set contains this set.
    set1 = {'bat', 'ball'}
    set2 = {'pad', 'gloves', 'ball', 'bat', 'wicket'}
    print(set1.issubset(set2))


def verify_isSuperset():
    # Report whether this set contains another set.
    set_a = {'ball', 'bat', 'wicket'}
    set_b = {'pad', 'gloves', 'ball', 'bat', 'wicket'}
    print(set_b.issuperset(set_a))


def add_num():
    set_1 = set()
    set_1.add("Gopi")
    print(set_1)


def remove_member():
    set_b = {'pad', 'gloves', 'ball', 'bat', 'wicket'}
    set_b.remove('pad')
    print(set_b)


# Return a new set of identical items from two sets
def new_set_identical():
    set1 = {'ball', 'bat', 'wicket', 'Goal', 'Over', 'Captain'}
    set2 = {'pad', 'gloves', 'ball', 'Goal', 'Over'}
    print(set1.intersection(set2))  # Output : {'Over', 'Goal', 'ball'}
    # Here other than common elements rest other elements are removed


# Get Only unique items from two sets
def uniqueItems():
    set1 = {'1', '2', '3'}
    set2 = {'4', '5', '6', '1', '2'}
    print(set1 | set2)  # Output: {'2', '3', '5', '1', '4', '6'}
    # Here the duplicate elemets are removed and unique elements are printed


# Update the first set with items that don’t exist in the second set
def first_set():
    set1 = {'1', '2', '3'}
    set2 = {'2', '3', '5'}
    set1.difference_update(set2)
    print(set1)
    # It modifies this set by removing all the items that are also present in the specified sets.
    # Output: {'3', '1', '2'}


# Write a Python program to remove items 10, 20, 30 from the following set at once.
def remove_items():
    set1 = {10, 20, 30, 40, 50}
    set1.difference_update({10, 20, 30})
    print(set1)


# Return a set of elements present in Set A or B, but not both
def return_set():
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 10, 70}
    print(set1.symmetric_difference(set2))


# Check if two sets have any elements in common. If yes, display the common elements
def common():
    set1 = {10, 20, 30, 40, 50}
    set2 = {60, 70, 80, 90, 10}
    # Method A:
    if set1.isdisjoint(set2):
        print("2 Sets have no common elements")
    else:
        print("2 sets have common elements")
        print(set1.intersection(set2))

    # Method B:
    set1.intersection_update(set2)
    print(set1)


# Update set1 by adding items from set2, except common items
def common_items():
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    print(set1.symmetric_difference_update(set2))
    print(set1)


# Remove items from set1 that are not common to both set1 and set2
def notCommon():
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}



def union_set():
    """ Python – Find union of multiple sets """
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    print(set1.union(set2))


#
def duplicate_sets():
    """ Python Program to Find Duplicate sets in list of sets """
    list1 = [{1, 2, 3}, {4, 5, 6}, {1, 2, 3}]


intersection_of_sets()