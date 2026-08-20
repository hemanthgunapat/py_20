from unittest import result

1.#A banking application has a function check_balance(). Create two decorators: verify_user,
# which prints "User verified", and log_transaction, which prints "Transaction logged".
# Apply both decorators to check_balance() and display "Balance displayed" from the original function.
def decorator1(func):
    def wrapper():
        print("User verified")
        func()
    return wrapper
def decorator2(func):
    def wrapper():
        print("Transaction logged")
        func()
    return wrapper
@decorator1
@decorator2
def check_balance2():
        print("Balance displayed")
check_balance2()

2.#An online examination system has a function start_exam(student). Before allowing the student
# to start the exam, the system must verify the student’s login and then log the exam activity.
# Create two decorators, login_required and log_activity, and apply both decorators to start_exam().
# The function should finally display "Exam started for <student>".
def student_decorator1(func):
    def wrapper():
        print("login_required")
        func()
    return wrapper
def student_decorator2(func):
    def wrapper():
        print("log_activity")
        func()
    return wrapper
@student_decorator1
@student_decorator2
def start_exam():
    print("Exam started for <hemureddy>")
start_exam()

3.#An online shopping application has a function place_order(). Create two decorators: login_check
# to print "Login verified" and order_log to print "Order recorded". Apply both decorators to place_order()
# and display "Order placed successfully" from the original function.
def place_decorator1(func):
    def wrapper():
        print("Login verified")
        func()
    return wrapper
def place_decorator2(func):
    def wrapper():
        print("Order recorded")
        func()
    return wrapper
@place_decorator1
@place_decorator2
def place_order():
    print("Order placed")
place_order()
