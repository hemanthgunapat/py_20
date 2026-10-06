9#.
class BankAccount:
    def _init_(self,balance):
        self.__balance = 0
        self.balance = balance

    @property
    def balance(self):
        pin=int(input("enter pin"))
        if pin==1234:
            return self.__balance
        else:
            self.count-=1
            return f"Access denied . you made a unsccessful attempts".{self.count}
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = value
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance = self.__balance + amount
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.balance = self.__balance - amount
    acc = BankAccount(100)
    print("Initial:", acc.balance)
    acc.deposit(50)
    print("After deposit:", acc.balance)
    acc.withdraw(30)
    print("After withdraw:", acc.balance)


10#.
import math
class Circle:
    def _init_(self, radius=1):
        self.__radius = 0
        self.radius = radius

    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self.__radius = value
    @property
    def area(self):
        return math.pi * (self.__radius ** 2)
    @property
    def circumference(self):
        return 2 * math.pi * self.__radius

    c = Circle(5)
    print("Radius:", c.radius)
    print("Area:", c.area)
    print("Circumference:", c.circumference)

    c.radius = 10
    print("\nAfter changing radius to 10:")
    print("Radius:", c.radius)
    print("Area:", c.area)
    print("Circumference:", c.circumference)

11#.
class Person:
    def _init_(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name

    @full_name.setter
    def full_name(self, name):
        parts = name.split(" ")

        self.first_name = parts[0]
        self.last_name = parts[1]


person = Person("Hemanthreddy", "Gunapati")
    print("First name:", person.first_name)
    print("Last name:", person.last_name)
    print("Full name:", person.full_name)

    person.full_name = "Rahul Kumar"

    print("\nAfter changing full name:")
    print("First name:", person.first_name)
    print("Last name:", person.last_name)
    print("Full name:", person.full_name)