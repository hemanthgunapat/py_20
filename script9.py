# Design a Python program for a supermarket billing system. Create a function calculate_total(prices)
# that accepts the prices of multiple items and returns their total cost. Then define a function
# apply_discount(*amount) that applies a 10% discount if the total exceeds 1500. Finally, create a
# function final_bill(*details) that accepts keyword arguments such as amount, tax, and packing_charge,
# and returns the final payable bill. Display the final amount using a single nested function call.

def calculate_total(*price):
    total=0
    for charge in charges:
        total+=charge
    return total
def apply_discount(*price):
    total=price[0]
    for i in amount:
       if total>1500:
           return total - total *0.1
       return total
def final-bill(**details):
    total_bill=0
    for sevrice,charge in details.items():
        total_bill+= charge
    print("your final bill is $",total_bill)
item1 =int(input("enter your first item price:"))
item2 =int(input("enter your second item price:"))
item3 =int(input("enter your third item price:"))
total =calculate_total(item1,item2,item3)
