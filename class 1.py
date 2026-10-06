# from encodings.punycode import insertion_unsort
class phone:
    x="Anroid"
    c=0
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
        phone.c+=1
obj=phone("vivo",1000)
print(phone.c)
from sys import displayhook
from threading import BoundedSemaphore


1.#A bank wants to create a simple system to store customer account details.Create a class Bank Account
# with a class variable bank_name = "ABC Bank" and instance variables account_holder, account_number,
# and balance. Initialize the instance variables using a constructor. The constructor should validate
# that the initial balance is not negative; if it is negative, set the balance to 0. Create two account
# objects and display their details.
class BankAccount:
    bank_name="ABC bank"
    def __init__(self,account_holder,account_number,balance):
        self.account_holder=account_holder
        self.account_number=account_number
        self.balance=balance
        if balance<0:
            self.balance=0
        else:
            self.balance=balance
a1 = BankAccount("Hemu", 1007628274, 1500)
a2 = BankAccount("Teja", 1234567887, -4000)
def display(self):
    print(a1.bank_name)
    print(a1.account_holder)
    print(a1.account_number)
    print("Balance",self.balance)
    print()
def disply(self):
    print(a2.bank_name)
    print(a2.account_holder)
    print(a2.account_number)
    print("Balance",self.balance)
    print()
display(a1)
display(a2)

2.#A college wants to maintain student records. Create a class Student with a class variable
# college = "ABC College" and instance variables name, roll_no, and marks. Initialize these values
# using _init_(). The constructor should validate that marks are between 0 and 100; if invalid marks
# are provided, set them to 0. Create three student objects and display their details.
class student:
    college = "ABC college"
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
        if marks>=0 and marks <=0:
            self.marks=marks
        else:
            self.marks = 0
s1 = student("Alice", 123, 89)
s2 = student("Bob", 568, -90)
s3 = student("Henry", 9392, 78)
print(s1.__dict__)
print(s2.__dict__)
print(s3.__dict__)


3.#An online store wants to maintain a list of products added to its system. Create a global
# list products = []. Create a class Product with a class variable store_name = "ABC Store" and
# instance variables name, price, and quantity. Initialize the values using the constructor and
# validate that price and quantity cannot be negative. Whenever a product object is created, add its
# name to the global products list. Create three products and display the product details and the
# complete product list.
class product:
    products = []
    store_name= "ABC store"
    def __init__(self,name,price,quantity):
        self.name=name
        if price>0 and quantity>0:
            self.price=price
            self.quantity=quantity
        else:
            print("Invalid Price or Quantity")
        product.products.append(name)
p1=product("Laptop",10000,2)
p2=product("Mouse",5000,5)
p3=product("PS5",4000,40)
print(p1.__dict__)
print(p2.__dict__)
print(p3.__dict__)

4.#A company wants to generate basic salary information when employee objects are created.
# Create a class Employee with class variables company = "TechCorp" and employee_count = 0.
# The constructor should accept name, department, salary, and experience. Validate that salary
# and experience are not negative. Based on experience, calculate a bonus inside the constructor:
# employees with more than 5 years receive 15%, employees with 3–5 years receive 10%, and employees
# with less than 3 years receive 5%. Create an instance dictionary pay_details containing the
# employee’s name, salary, experience, bonus, and final salary. Generate an employee ID using
# employee_count. Create three employee objects and display their _dict_.
class employee:
    company = "TechCorp"
    empolyee=0
    def __init__(self,name,department,salary,experience):
        employee.empolyee
        self.name=name
        self.department=department
        if salary < 0 and experience < 0:
            self.salary=salary
            self.experience=experience
        if experience > 5:
            bonus_present = 0.5
        elif 3<= experience <=5:
            bonus_present = 0.10
        else:
            bonus_present = 0.05
        final_salary= salary + bonus_present
        self.empolyee=employee.empolyee

5#.An online learning platform creates student enrollment objects. Create a class Enrollment
# with class variable platform = "LearnOnline" and enrollment_count = 0. The constructor should
# accept student_name, course, and age. If the student’s age is 18 or above, set an instance
# variable status = "Registered"; otherwise set it to "Rejected". Increase enrollment_count only
# for registered students. Create three objects and use isinstance() to check which objects are
# instances of Enrollment.

class Enrollment:
    platform = "LearnOnline"
    enrollment_count = 0
    def __init__(self, student_name, course, age):
        self.student_name = student_name
        self.course = course
        self.age = age
        if age >= 18:
            self.status = "Registered"
            Enrollment.enrollment_count += 1
        else:
            self.status = "Rejected"
student1 = Enrollment("Rahul", "Python", 20)
student2 = Enrollment("Priya", "Data Science", 17)
student3 = Enrollment("Arjun", "Web Development", 22)
print(student1.student_name, student1.course, student1.status)
print(student2.student_name, student2.course, student2.status)
print(student3.student_name, student3.course, student3.status)
print("Platform:", Enrollment.platform)
print("Registered Students:", Enrollment.enrollment_count)
print("student1 is Enrollment:", isinstance(student1, Enrollment))
print("student2 is Enrollment:", isinstance(student2, Enrollment))
print("student3 is Enrollment:", isinstance(student3, Enrollment))