units = int(input("Enter the units please: "))
if(units<=100):
    print("Total bill is 0")
elif(units>100 and units<200):
    print((units-100)*5)
elif(units>200):
    print((500)+((units-200) *10))




#Print the last digit
var = int(input("Enter numb: "))
print(var % 10)