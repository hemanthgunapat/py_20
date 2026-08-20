# from Lambda1 import square
from unittest import result

1#. PARAMETERS + LAMBDA: Write a function apply_operation(a, b, op)
# #where op is a lambda. Call it with operations for add, subtract, and multiply.
def apply_operations(a,b,op):
    return op(a , b)
print(apply_operations(10, 20, lambda x,y:x-y))

2.#*args + RECURSION: Write a recursive function that takes * args of numbers and returns
# #their sum WITHOUT using the built - in sum().
def recursion(*args):
    if not args:
         return 0
    return args[0]+recursion(*args[1:])
print(recursion(1,2,3,4,))
print(recursion(10,20,30))

3.#DEFAULT + KEYWORD + LAMBDA: Write a function make_greeting(name, prefix='Hello', formatter=lambda x: x) that
# #applies formatter to the final greeting string.Test with str.upper as the formatter.
def make_greeting(name,prefix='hello',formatter=lambda x:x):
    formatter=f"{prefix},{name}!"
    return formatter
print(make_greeting('alice'))
print(make_greeting('hello',formatter=str.upper))

4.#map() + filter() + lambda: Given a list of integers from 1 to 20, use filter() to keep multiples of 3,
# #then use map() to square them.
def apply_all(func,value):
    for i in func:
        print(i(value))
numbers=list(range(1,20))
mul_of_3=filter(lambda x:x%3==0,numbers)
square=list(map(lambda x:x**2,mul_of_3))
print(square)

5.# FUNCTION REFERENCE + HIGHER ORDER: Create a list of lambda functions [double, triple, quadruple].
# # Write a function apply_all(funcs, value) that applies each in sequence and returns the final result.
l=[
     lambda x:x*2,
     lambda x:x*3,
     lambda x:x*4,
    ]
def apply_all(func,value):
     for i in func:
         value=i(value)
     return value
print(apply_all(l,2))

10.#  ALL CONCEPTS: Write a function calculator(*args, operation='add', **options) that: (a) uses *args to
# # collect numbers,(b) uses a default 'add' operation, (c) supports operations: 'add', 'multiply', 'max', 'min'
# # using a dict of lambda functions, (d) if options contains show_steps=True, prints each step of the calculation.
def calculate(*args,operation='add',**options):
    op = {
        'add':lambda x,y:x+y,
        'mul':lambda x,y:x*y,
        'max':lambda x,y:x if x>y else y,
        'min':lambda x,y:x if x<y else y
        }
    func=op[operation]
    res=args[0]
    for i in args[1:]:
        if options.get("show.steps"):
            print(res,i,options.get(":",func(res,i)))
        res=func(res,i)
    return res
print(calculate(1,2,3,4,5,6))
print(calculate(1,2,3,operation='mul'))

8.#FULL PIPELINE: Build a mini data pipeline. Start with a list of student dictionaries
# # [{name, score}]. Use filter() to keep scores >= 60, map() to add a 'grade' key ('Pass'), and
# # sorted() to sort by score descending. Print the final result.
students=[
    {"name":"hemu","score":90},
    {"name":"manisankar","score":120},
    {"name":"syam","score":30},
    {"name":"khadri","score":70}
        ]
print(list(map(lambda x:{**x, 'grade':'pass'},list(filter(lambda x:x['score']>60,students)))))
print(sorted(students,key=lambda x:x['score'],reverse=True))
print(students)

6.#RECURSION + DEFAULT PARAMETER: Write a recursive function flatten(lst, depth=1)
# that flattens a nested list up to the given depth. Example: flatten([[1,[2]],3],depth=2) → [1, 2, 3].
def flatten(lst, depth=1):
    return []
for i in list:
    if isinstance(i,list) and depth > 0:
        result.extend(flatten(i,depth - 1))
    else:
        result.append(i)
print(flatten([[1,[2]],3]))



