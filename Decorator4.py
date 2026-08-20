1.# Create functions add(a, b), subtract(a, b) and multiply(a, b).
# Create a function calculate(operation, a, b) that accepts a function reference and performs the selected operation.
# Use lambda functions to perform:
# * Square of a number
# * Cube of a number
# * Double of a number
# Add a decorator log_operation that prints "Operation started" before execution and "Operation completed" after execution.
def log_operation(func):
    def wrapper(*args, **kwargs):
        print("Operation started")
        result = func(*args, **kwargs)
        print("Operation completed")
        return result
    return wrapper
@log_operation
def add(a ,b):
    return a+b
@log_operation
def subtract(a,b):
    return a-b
@log_operation
def multiply(a,b):
    return a*b
@log_operation
def caliculate(operation,a,b):
    return operation(a,b)
square=lambda x:x**2
cube=lambda x:x**3
double=lambda x:x*2
print("add:",caliculate(add,10,5))
print("sub:",caliculate(subtract,10,5))
print("mul:",caliculate(multiply,10,5))
print("square:",square(5))
print("cube:",cube(5))
print("double:",double(5))

2.#Create a function process_marks(marks, operation) where operation is a function reference.
# Use lambda functions to:
# * Add 5 grace marks
# * Double each mark
# * Find whether a mark is greater than 40
# Create a decorator that prints "Processing started" and "Processing completed".
def processing_decorator(func):
    def wrapper(*args, **kwargs):
        print("Processing started")
        result = func(*args, **kwargs)
        print("Processing completed")
        return result
    return wrapper
@processing_decorator
def process_marks(marks,operation):
    return operation(a,b)