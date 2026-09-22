# Instance Variables and Methods
class Dog:
    # constructor 
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says woof")
    
dog1 = Dog('Buddy',3)

dog1.bark()
print(dog1.name, dog1.age)






# Modelling a Bank Account

class BankAccount:
    # constructor
    def __init__(self,owner,balance=0) -> None:
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance = self.balance + amount
        print(f"{amount} is deposited. New Balance is {self.balance}")

    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance = self.balance - amount
            print(f"{amount} is withdrawn. New Balance is {self.balance}")

    def get_balance(self):
        return self.balance


account = BankAccount("Rohith",5000)

account.deposit(500)

account.withdraw(6000)

account.withdraw(300)

print(account.get_balance())