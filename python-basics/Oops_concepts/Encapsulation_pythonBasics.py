
'''
Encapsulation means keeping data and the methods that work on that data together inside a class, 
and controlling how that data is accessed or changed.
Encapsulation is like protecting the inside details of an object and only allowing access 
through specific methods.
'''
print('=====================================Private Variable ============================= \n')
class BankAccount:
    def __init__(self,balance) -> None:
        self.__balance = balance  #Private variable

    def get_balance_internal_fun(self):
        return self.__balance # 5000 #10000


class SavingsAccount(BankAccount):
    def __init__(self, balance,interest_rate) -> None:
        super().__init__(balance)
        self.__interest_rate = interest_rate

    def show_account_details(self):
        '''
        AttributeError: 'SavingsAccount' object has no attribute '_SavingsAccount__balance'. 
        Did you mean: '_BankAccount__balance'?
        '''
        print("balcnace >>>>>>>>", self.__balance)
        print(f"interest rate : {self.__interest_rate}")

def get_balance(account):
    return account._BankAccount__balance # 5000


account1 = BankAccount(5000)
print(account1.get_balance_internal_fun())
'''
AttributeError: 'BankAccount' object has no attribute '__balance'. Did you mean: 'get_balance'?
'''
# print(account1.__balance)
print(get_balance(account1)) # 5000

account2 = BankAccount(10000)
print(get_balance(account2)) # 10000

savings1 = SavingsAccount(5000, 5)

# savings1.show_account_details()

print('=====================================Private Variable ============================= \n')


print('=====================================Protected Variable ============================= \n')

class Student:
    def __init__(self, name , marks) -> None:
        self._name = name  # protected variable
        self._marks = marks # protected variable

    def show_marks(self):
        print(f"Marks : {self._marks}")


class CollegeStudent(Student):
    def __init__(self, name, marks) -> None:
        super().__init__(name, marks)

    def show_student_details(self):
        print(f"Name : {self._name}")
        print(f"Marks : {self._marks}")


collegestudent1 = CollegeStudent("Rohith",100)
# trying to access protected varible outside
print(collegestudent1._name , collegestudent1._marks)

student1 = Student("Rohith",100)
# trying to access protected varible outside
print(student1._name , student1._marks)

print('=====================================Protected Variable ============================= \n')


print('=====================================Getter and Setter Methods ============================= \n')

class Student:
    def __init__(self,name , marks) -> None:
        self.__name = name   # private variable
        self.__marks = marks     # private variable

    # Getter method
    def get_marks(self):
        return self.__marks

    # Setter method
    def set_marks(self,marks):
        if marks >=0 and marks <=100:
            self.__marks = marks
        else:
            print("Marks should be between 0 and 100")


student1 = Student("rohith",80)
print(student1.get_marks())

student1.set_marks(95)
print(student1.get_marks())

student1.set_marks(950)

print('=====================================Getter and Setter Methods ============================= \n')