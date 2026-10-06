class A:
    c1 = "hey"
    c2 = 123
    def _init_(self, x, y):
        self.x = x
        self.y = y
class B(A):
    c3 = True
    def _init_(self, z, x, y):
        self.z = z
        # A._init_(self,x, y)
        super()._init_(x, y)
b = B(10, 20, 30)
print(b.c1)
print(b.c2)
print(b.c3)
print("z :",b.z)
print("x :",b.x)
print("y :",b.y)

class A:
    def _init_(self, x):
        self.x = x
class B(A):
    def _init_(self, x , y):
        self.y = y
        # A._init_(self, x)
        super()._init_(x)
class C(B):
    def _init_(self, x, y , z):
        self.z = z
        # B._init_(self, x, y)
        super()._init_(x, y)
c = C(10,20,30)
print("x: ",c.x)
print("y :",c.y)
print("z :" ,c.z)