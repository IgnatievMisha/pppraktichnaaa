#1
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f'name: {self.name}, age: {self.age}')
Student = Student(name = "Vasya", age = 20)
Student.info()
#2
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        print(f'S = {self.radius*self.radius*3.14}')
Circle = Circle(radius = 5)
Circle.area()
#3
class Animals:
    pass
class Dog(Animals):
    def sound(self):
        print("Woof")
bobik = Dog()
bobik.sound()
#4
class BankAccount:
    def __init__(self, balance, owner):
        self.balance = balance
        self.owner = owner
    def deposit(self):
        self.balance = self.balance + 100
        print(self.balance)
    def withdraw(self):
        self.balance = self.balance - 100
        if self.balance>0:
            print(self.balance)
        else:
            print("ERROR")
bank = BankAccount(balance = 500, owner = "boss")
bank.deposit()
bank.withdraw()
