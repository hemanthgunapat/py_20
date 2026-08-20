
'''create a python application to design a function for a food delivery application where the customer name is
taken as a positional argument and the audio type default argument function should accpet multiple food items
order by the customer using positional arguments and additional details such as address, payment mode,delivery
instrustion and using keyword arguments the function should display the complete order summary include the
customer details list it        ems ordered, total number of items, and all additional items'''

def swiggy(customer_name, order_type="regular" ,*items, **customer_details):
    print("hi",customer_name)
    print("your order type is :",order_type)
    print("your cart:")
    total_bill =0
    for item in items:
        print(item[0]," : Rs.",items[1])
        total_bill += item[1]
    print("total items in cart :",len(items))
    print("your total bill is : Rs.",total_bill)
    print("additional details:")
    for details,description in customer_details.items():
        print(details," :rs.",description)
swiggy (customer_name="Hemanth", order_type="swiggy one", items=["Burger",250],["Fries",60] ,["Coke",40],payment_mode ="UPI")
delivary_instruction =("Don't ring at bell"),cutlery =("yes,provide")