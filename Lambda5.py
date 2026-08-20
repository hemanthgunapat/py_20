#1. Given a list of product prices, write a program to filter prices above ₹500,
# then apply a 10% discount using map(), and compute the final total bill using reduce().
from functools import reduce
l8=[100,200,300,400,600,700]
price=list(filter(lambda x:x>500,list(map(lambda x:x-x*0.1,l8))))
print(price)
print(reduce(lambda x,y:x+y,price))

#2. Given a list of numbers, write a program to filter negative numbers, then convert
# them into positive numbers using map(), and find their sum using reduce().
l=(3,5,7,8,9,11,12)
positive=list(filter(lambda x:x>0,list(map(lambda x:x*2,l))))
print(positive)