1.#Create a function get_message() that returns "hello user". Write a decorator
# using @ syntax that converts the output to uppercase.
def msg_decorator(func):
    def wrapper(item):
        func(item)
    return wrapper
@msg_decorator
def get_message(item):
    return item.upper
print(get_message("hello user"))

2.#     Create a function get_number() that returns 10
#   Use a decorator to return double the value.
def number_decorator(func):
    def wrapper():
        value=func()
        return value *2
    return wrapper
@number_decorator
def get_number():
    return 10
print(get_number())

3.# Create a function place_order(item)
#  Use a decorator to print:
# * “Order process started”
# * “Order process completed”
def place_order_decorator(func):
    def wrapper(item):
        print("Order process started")
        result=func(item)
        print("Order process completed")
        return result
    return wrapper
@place_order_decorator
def place_order(item):
    return item
print(place_order("loli pop"))

4.#Create a function login(username)
#    Use a decorator to print:
#    * “Authenticating user…”
#   * “Login successful”
def login_decorator(func):
    def wrapper(username):
        print("Authenticating user...")
        result=func(username)
        print("Login successful")
        return result
    return wrapper
@login_decorator
def login(username):
    return username
print(login("hemureddy"))

5.#     Create a function send_message(msg)
#    Use a decorator to print:
#   * “Sending message…”
#    * “Message sent”
def msg_decorator(func):
    def wrapper(msg):
        print("Sendimg message")
        result=func(msg)
        print("Message sent")
        return result
    return wrapper
@msg_decorator
def msg(msg):
    return msg
print(msg("khadri ,syam are my frnds"))

6.#     Create a function add(a, b)
#    Use a decorator to print:
#   * “Calculating sum…”
#  * “Calculation done”
def add_decorator(func):
    def wrapper(a,b):
        print("Calculating sum")
        result=func(a,b)
        print("Calculating done")
        return result
    return wrapper
@add_decorator
def add(a,b):
    return a + b
print(add(5,5))

7.#     Create a function apply_discount(price)
#  Use a decorator to print:
# * “Applying discount…”
#* “Discount applied”
def price_decorator(func):
    def wrapper(price):
        print("Apply discount")
        result= func(price)
        print("Discount applied")
        return result
    return wrapper
@price_decorator
def apply_discount(price):
    return price * 0.90
print(apply_discount(100))
