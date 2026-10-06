def intro():
    print("This is py-20")
def decorated1(func):
    def wrapper1():
        print("hi")
        func()
    return wrapper1
intro=decorated1(intro)
intro()

1.# Create a function start_system()
 #   Write a decorator that prints:
  # * “System started successfully”
    # after execution
def intro():
    print("System started successfully")
def dec_system1(func):
    def wrapper1():
        print("after exeution")
    return wrapper1
intro=dec_system1(intro)
intro()
2.#     Create a function show_message()
  #  Write a decorator that prints:
   # * “Welcome!” before
    #* “Goodbye!” after

#3.     Create a function make_payment()
 #   Write a decorator that prints:
  #  * “Payment initiated”
   # * Payment successful

def make_payments():
    print("payment initiated")
def dec_system(func):
    def wrapper1():
        print("Payment succesful")
    return wrapper1
make_payments=dec_system(make_payments)
make_payments()