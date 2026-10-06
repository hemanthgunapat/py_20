class payment:
    def __init__(self,amount):
        self.amount=amount
    def process(self):
        print("Processing payment")
class creditcard(payment):
    def process(self):
        print("Processing using Credit card:",self.amount)
class UPI(payment):
    def process(self):
        print("Processing using UPI:",self.amount)
class NetBanking(payment):
    def process(self):
        print("Processing using Net Banking:",self.amount)
def checkout(payment):
    payment.process()

p1=creditcard(3000)
p2=UPI(200)
p3=NetBanking(1000)

checkout(p1)
checkout(p2)
checkout(p3)