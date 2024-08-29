"""
class Student:
    CollageName = "PRPCEM , AMRAVATI"
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print("Welcome student,",self.name)

s1 = Student("Karan",91)
s1.welcome()
"""

            # STATIC METHODS

"""
class Student:
    @staticmethod
    def collage():
        print("PRPCEM")
"""
           # BANK ACCOUNT USING OOPS
"""
class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc

    def debit(self,amount):
        self.balance -= amount
        print("Rupees:", amount,"Was debited")
        print("Total balance =",self.get_balance())


    def credit(self,amount):
        self.balance -= amount
        print("Rupees:", amount,"Was crediated")
        print("Total balance =",self.get_balance())

    def get_balance(self):
        return self.balance

acc1 = Account(100000 , 12345)
acc1.debit(1000)
acc1.credit(500)
#print(acc1.balance)
#print(acc1.account_no)

"""

            # CALCULATION OF AREA OF CIRCLE IN PYTHON
"""
class Circle:
    def __init__ (self,radius):
        self.radius = radius

    def area(self):
        return (22/7) * self.radius ** 2
    def perimeter(self):
        return 2 * (22/7) * self.radius

c1 = Circle(21)
print(c1.area())
print(c1.perimeter())

"""
