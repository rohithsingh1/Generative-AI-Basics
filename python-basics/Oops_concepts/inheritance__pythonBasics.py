class Car:
    # constructor
    def __init__(self,windows,doors,engineType) -> None:
        self.windows = windows
        self.doors = doors
        self.engineType = engineType

    def drive(self):
        print(f"The person will drive the {self.engineType} car")


class Tesla(Car):
    def __init__(self, windows, doors, engineType,isSelfDriving) -> None:
        super().__init__(windows, doors, engineType)
        self.isSelfDriving = isSelfDriving

    def selfDriving(self):
        print(f"Tesla supports self driving : {self.isSelfDriving}")



tesla1 = Tesla(4,5,"Petrol",True)
print(tesla1.selfDriving())
print(tesla1.drive())


'''
Multiple Inheritance
When a class inherits from more than one base class
'''

class Animal:
    def __init__(self,name) -> None:
        self.name = name

    def speak(self):
        print("subclass must implement the base class")


class Pet:
    def __init__(self,owner) -> None:
        self.owner = owner


class Dog(Animal,Pet):
    def __init__(self, name,owner) -> None:
        Animal.__init__(self,name)
        Pet.__init__(self,owner)

    def speak(self):
        print(f"{self.name} says woof")
        Animal.speak(self)
        super().speak()



dog1 = Dog("shoppy","rohith")
dog1.speak()
print(dog1.owner)