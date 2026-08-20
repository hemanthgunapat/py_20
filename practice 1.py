#Design a Python program for a supermarket billing system. Create a function calculate_total(prices)
# that accepts the prices of multiple items and returns their total cost. Then define a function
# apply_discount(*amount) that applies a 10% discount if the total exceeds 1500. Finally, create a
# function final_bill(*details) that accepts keyword arguments such as amount, tax, and packing_charge,
# and returns the final payable bill. Display the final amount using a single nested function call.

def calculate_total(prices):
    return sum(prices)
def apply_discount(*amount):
    total = amount[0]
    if total > 1500:
        total = total - (total * 0.10)
    return total
def final_bill(**details):
    amount = details.get("amount",0)
    tax = details.get("tax",0)
    packing_charge = details.get("packing_charge",0)
    return amount+tax+packing_charge
price=[500,700,800]
print("final payable bill = $",final_bill(amount=apply_discount(calculate_total(price)),tax=0,packing_charge=20))

1.#Write a function simple_interest(principal, rate=5, time=1) to calculate simple interest.
# Demonstrate different function calls by passing only required arguments and then overriding default values.
def simple_interest(principal, rate=5, time=1):
    simple=(principal*rate*time)/100
    return simple
print("simple interest 1=",simple_interest(10000))
print("simple interest 2=",simple_interest(10000,time=3))
print("simple interest 3=",simple_interest(10000,rate=8,time=4))

2.#Create a function student_info(name, *subjects, **details) that prints a student’s name, subjects enrolled,
# and additional details like grade and school.
def student_info(name, *student, **details):
    print("name:",name)
    print("student:",student)
    print("details:",details)
student_info(name="hemu", student=["telugu", "english", "maths"],grade='A',details="adityadegreecollege")

3.#Write a function order_food(*items, **preferences) that accepts multiple food items and optional
# preferences like spice level or delivery time. Display the order summary.
