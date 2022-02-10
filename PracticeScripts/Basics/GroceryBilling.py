grocery_item_price = 0

print(''' ================================================
            Welcome to Grocery Billing 
 ================================================''')


def calculate_grocery():
    list_of_items = []
    global grocery_item_price
    for i in range(3):
        item = input("Enter the item name: ")
        list_of_items.append(item)
    for i in list_of_items:
        price = int(input("Enter the price of " + i + ": "))
        grocery_item_price = grocery_item_price + price


def verify_membership():
    calculate_grocery()
    list_of_mobile_numbers = [1234567890, 1234567891, 1234567892]
    mobile_number = int(input("Enter the phone number: "))
    for i in list_of_mobile_numbers:
        if mobile_number == i:
            print("Eligible for the membership discount 10%")
            discount = (grocery_item_price * 10) / 100
            total_bill = int(grocery_item_price-discount)
            total_savings = int(discount)
            print("Total bill amount: "+str(total_bill)+" Rs")
            print(("Your savings: "+str(total_savings))+" Rs")
            break
        elif mobile_number != i:
            print("Not a member, not eligible for discount")
            list_of_mobile_numbers.append(mobile_number)
            print(list_of_mobile_numbers)
            print("Total bill amount: "+str(grocery_item_price)+" Rs")
            break


verify_membership()
