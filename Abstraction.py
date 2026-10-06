1#.
# Create an abstract class Payment with an abstract method pay(amount) Create:
# • UPI
# • CreditCard
# • Cash
# Each class should implement pay() differently.

from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
class UPI(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")
class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")
class Cash(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Cash")
h1= UPI()
h2= CreditCard()
h3= Cash()
h1.pay(500)
h2.pay(1000)
h3.pay(200)

2#.
# Create an abstract class Notification with:
# send(message)
# Create:
# •	Email
# •	SMS
# •	WhatsApp
# Each child class should implement send() differently

from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self,message):
        pass
class Email(Notification):
    def send(self,message):
        print("Sending Email:",message)
class SMS(Notification):
    def send(self,message):
        print("Sending SMS:",message)
class Whatsapp(Notification):
    def send(self,message):
        print("Sending Whatsapp:",message)
email=Email()
sms=SMS()
whatsapp=Whatsapp()

email.send("Dear Hemu*")
sms.send("Your OTP is 31210")
whatsapp.send("Hi,Darling")

3#.
# Create an abstract class LoginSystem with:
# login(username, password)
# logout()
# Create:
# •	AdminLogin

from abc import ABC,abstractmethod
class Loginsystem(ABC):
    @abstractmethod
    def login(self,username,password):
        pass
    @abstractmethod
    def logout(self):
        pass
class Adminlogin(Loginsystem):
    def login(self,username,password):
        if username =="admin" and password=="admin3121":
            print("Admin Login Successful")
        else:
            print("Invalid Username or password")
    def logout(self):
        print("Admin logged out")
class Userlogin(Loginsystem):
    def login(self, username, password):
        if username == "user" and password == "user3121":
            print("User Login successful")
        else:
            print("Invalid User Username or Password")
    def logout(self):
        print("User Logged Out")

h1= Adminlogin()
h1.login("admin","31210")
h1.logout()
h2=Userlogin()
h2.login("user","user3121")
h2.logout()

4#.
# Create an abstract class BankAccount with two abstract methods:
# deposit(amount)
# withdraw(amount)
# Create:
# •	SavingsAccount
# •	CurrentAccount
# Maintain the balance using an instance variable.

from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, balance):
        self.balance = balance
    @abstractmethod
    def deposit(self, amount):
        pass
    @abstractmethod
    def withdraw(self, amount):
        pass
class SavingsAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
        print("Balance:", self.balance)
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
            print("Balance:", self.balance)
        else:
            print("Insufficient Balance")
class CurrentAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
        print("Balance:", self.balance)
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
            print("Balance:", self.balance)
        else:
            print("Insufficient Balance")

savings = SavingsAccount(5000)
savings.deposit(2000)
savings.withdraw(1000)
print()
current = CurrentAccount(10000)
current.deposit(5000)
current.withdraw(3000)