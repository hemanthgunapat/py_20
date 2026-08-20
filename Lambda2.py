l=[1,2,3,4]
p=list(map(lambda x:x**2,l))
print(p)

l=[1,2,3,4]
l1=[1,2,3,4]
l2=[5,6,7,8,]
l3=list(map(lambda x,y:x+y,l1,l2))
print(l3)

l1=[1,2,3,4]
l2=[5,6,7,8]
l3=list(map(lambda x,y:x//2,l1,l2))
print(l3)

x=[1,2,3,4]
p=list(map(lambda x:x**2,x))
print(p)
print(list(filter(lambda x:x%2==0, list(map(lambda x:x**2,x)))))

