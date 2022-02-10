import re


def searchText():
    test = "GokheDie3"
    exp1 = '[^[a-b](@)?.com$'
    exp2 = re.compile("[A-Za-z0-9]+")

    if exp2.fullmatch(test) is not None:
        print("Pass")
    else:
        print("Fail")

def isCap(a,b):

    if re.match(a,b,re.IGNORECASE):
        print("Pass")
    else:
        print("Fail")
isCap("Feb","feb")
print("hi")