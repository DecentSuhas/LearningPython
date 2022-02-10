a, b, c = 29, 11, 49

a1=44
b1=a1
print(id(a1))
print(id(b1))
a1=44
print(id(a1))

global city

def printDetails():
    city = "Bangalore"
    age = 22
    fname = "Bob"
    lname = "Parike"
    name = fname,lname
    rollNum = 123,4442,343

    print("City: ",city,"Age: ",age,"Name: ",name)
    print("City: "+city)
    print(rollNum)
    rollNum = 233
    print(rollNum)

printDetails()