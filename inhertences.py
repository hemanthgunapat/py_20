# Create a Bank class with:
# • balance variable
# • deposit()
# • withdraw()
# • check_balance()
# Create a User class that inherits Bank and displays the user's name. Perform
# deposit, withdrawal, and balance check.
1#.
class Bank:
    def _init_(self, balance):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Dear {self.name},\nYour account has been credited with Rs.{amount} successfully.")
    def withdraw(self, amount):
        self.balance -= amount
        print(f"Dear {self.name},\nYour account has been debited with Rs.{amount} successfully.")
    def check_balance(self):
        print(f"Dear {self.name},\nYour current available balance is Rs.{self.balance}.")

class User(Bank):
    def _init_(self, name,balance):
        self.name = name
        super()._init_(balance)
user1 = User("hemu", 10000)
user2 = User("syam", 120000)
print(user1._dict_)
print(user2._dict_)
print(user1.name)
print(user2.name)
user1.deposit(5000)
user1.check_balance()
user2.withdraw(2000)
user2.deposit(10000)
user2.check_balance()

2#.
class Employee:
    def _init_(self, emp_name, salary):
        self.emp_name = emp_name
        self.salary = salary
    def display_details(self):
        print(f"Employee Name: {self.emp_name}, Salary: {self.salary}")

class Manager(Employee):
    def bonus(self):
        self.salary += self.salary * 0.1
alice = Manager("Alice", 15000)
alice.display_details()
alice.bonus()
alice.display_details()

3#.
class A:
    def _init_(self):
        self.x = 10
        self.y = 20
        self.z = 30
        self.count = 40
    def check_even(self, val):
        if val % 2 == 0:
            print("Even")
        else:
            print("Odd")
class B:
    def _init_(self, count):
        self.count = count
    def m1(self):
        obj = A()
        obj.check_even(self.count)
b = B(100)
print(b.count)
b.m1()
print(b.count)
