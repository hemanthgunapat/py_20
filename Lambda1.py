add=lambda x,y:x+y
print(add(10,20))

square=lambda x:x**2
print(square(5))
print(square(4))

l=[3,7,4,6,29,9,14,6]
l.sort(key=lambda x:x)
print(l)

fruits=[(1,'bananna'),(2,'apple'),(3,'cherry')]
fruits.sort(key=lambda x:x[1])
print(fruits)
#1
cube=lambda x:x**3
print(cube(8))
print(cube(10))

#2
a=lambda x,y: x if x>y else y
print(a(4,5))

#3
add=lambda x,y:x+y
multiply =lambda a,b:a*b+add
