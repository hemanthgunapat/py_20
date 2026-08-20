# Given a list of product prices, write a program to:
# * Filter prices greater than ₹500
# * Apply a 10% discount to the filtered prices using map()
prices=[250,350,450,550,650]
l2=list(filter(lambda x:x>500,list(map(lambda x:x-x*0.1,prices))))
print(l2)

1.#Given a list of integers, write a program to filter even numbers and then multiply
# each of them by 3 using a single pipeline.
l=[22,33,45,64,32]
f=list(filter(lambda x:x%2==0,list(map(lambda x:x*3,l))))
print(f)

#reduce lambda
from functools import reduce
l=[1,2,3,4,7,9,14,16]
print(reduce(lambda x,y:x+y,l))

2.#Given a list of numbers, write a program to filter numbers greater than 20 and then square
# each of the filtered numbers using map().
l=[20,34,44,65,1,2]
print(list(filter(lambda x:x>20,list(map(lambda x:x**2,l)))))

#sorted(interable,key=function,reverse=)
students=[{"name":'alice','score':85},
          {"name":'harry','score':79},
          {"name":'candice','score':81}]
l=sorted(students,key=lambda x:x['score'])
print(l)
#

l1=['King','Hemu','Raju','Queen']
print(list(filter(lambda x:x[0].isupper(),l1)))
