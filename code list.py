#22/09/2026
from xml.dom.minidom import Element
2#.
l=[10,20,30,40,50,60,70]
l.insert(1,400)
print(*l)

3# Merge method and extend method
l1=[20,30,40,50,60,10]
l2=[30,40,50,30,20,10]
l3=l1+l2
print(l3)
k1=[10,30,40,50]
k2=[30,20,60,50]
k1.extend(k2)
print(k1)

4# Remove method
l=[20,30,50,70,90,10]
element=90
if element in l:
    l.remove(element)
print(l)

5#. Remove an element from a list using its index.
l=[3,4,6,7,8,9,2,10]
l.pop(5)
print(*l)

6#. find the index of a given element in a list.
l=[20,40,30,60,70]
n=70
if (n in l):
    k=l.index(n)
    print(k)

7#.count the number of occurrences of an element in a list.
l=[40,20,30,50,70,60]
k=l.count(20)
print(k)

8#.find the sum of the first and last elements of a list.
l=[55,66,77,88,99,22,44]
k=6
if k>0 and k<len(l):
    sum=0
    for i in range(k+1):
        sum=sum+l[i]
    print(sum)

10#.calculate the average of odd numbers in a list.
# l=[20,40,60,80,10,30,50]
# sum=0
# c=0
# for i in range(len(l)):
#     if (l[i]%2==1):
#         sum=sum+l[i]
#         c=c+1
# print(sum/c)

11#. print all prime numbers present in a list. 
l=[10,20,30,40,50,60]
sum=c=0
for i in range(len(l)):
    fc=0
    for j in range(i,l[i]+1):
        if (l[i]%j==0):
            fc+=1
    if (fc==2):
        print(l[i])