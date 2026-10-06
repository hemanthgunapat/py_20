def m1(start,stop):
    while start<=stop:
        yield start
        start+=1
x=m1(11,50)
print(next(x))
for i in x:
    print(i)

def g2():
    n=1
    while True:
        yield n
        n+=1
x=g2()
print(next(x))

def g2():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
x=g2()
print(next(x))
print(next(x))
print(next(x))
print(next(x))


l=[x for x in range(1,10)]
print(l)
s={x for x in range(1,10)}
print(s)
d={x:x*x for x in range(1,5)}
print(d)
print(type(d))
t=(x for x in range(1,5))
print(t)


l=[x*x for x in range(1,10)]
print(l)
print(type(l))
n={x*x for x in range(1,10)}
print(n)
print(type(n))
y={x:x*x for x in range(5,10)}
print(y)
print(type(y))
t=(x for x in range(1,10))
for i in t:
    print(i,end=" ")
    print(type(t))
g=(x for i in range(2) for x in range(1,5))
for i in g:
    print(i,end=" ")
h=(x for x in range(1,10) if x%2==0)
for i in h:
    print(i,end=" ")
print(max(x for x in range(1,10)if x%2==0))
print(sum(x for x in range(1,10)if x%2==0))
print(min(x for x in range(1,10)if x%2==0))