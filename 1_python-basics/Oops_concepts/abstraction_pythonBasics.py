from abc import ABC , abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print('Car start with a key')


class Bike(Vehicle):
    def start(self):
        print("Bike start with a button")


car1 = Car()
bike1 = Bike()

car1.start()
bike1.start()