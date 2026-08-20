#1. Given a list of tuples (name, marks), sort the list:
 #   * first by marks (descending)
  #  * then by name (ascending)
from functools import reduce

students=[("hemu",50),("syam",40),("khadri",90),("teja",100),("krishna",150)]
l=sorted(students,key=lambda x:(-x[1],x[0]))
print(l)

#2. Given a list of strings, sort them based on:
 #   * length of string
 #   * and then alphabetically
list=[("hemu"),("syam"),("khadri"),("teja")]
print(sorted(list, key=lambda x: (len(x))))

#3.Given a list of integers, filter numbers divisible by both 2 and 5,
#add 5 to each using map(), then find the product using reduce().
import functools
l1=[10,20,30,40,50,60,70]
s=list(map(lambda x:x+5,list(filter(lambda x: x % 2 == 0 and x % 5 == 0,l1))))
product=reduce(lambda x,y:x*y,s)
print(product)