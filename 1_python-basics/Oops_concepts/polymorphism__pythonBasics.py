'''
Method overriding allows a child class to provide a specific implementation of a method 
that is already defined
in its parent class.
'''

## Base Class
class Animal:
    def __init__(self) -> None:
        pass

    def speak(self) -> str:
        return "Sound of the animal"

## Derived Class 1
class Dog(Animal):
    def __init__(self) -> None:
        super().__init__()

    def speak(self) -> str:
        return "Woof!"


dog1 = Dog()
print(dog1.speak())



'''
polymorphism with functions and methods
'''
class Shape:
    def __init__(self) -> None:
        pass

    def area(self):
        print("The area of the figure")



class Rectangle(Shape):
    def __init__(self,width , height) -> None:
        super().__init__()
        self.width = width
        self.height = height

    def area(self):
        print(f"Area of the Rectangle with width : {self.width} , height : {self.height} is {self.width * self.height}")



class Circle(Shape):
    def __init__(self,radius) -> None:
        super().__init__()
        self.radius = radius

    def area(self):
        print(f"Area of the Circle with radius : {self.radius} is {3.14 * self.radius * self.radius}")


'''
function that demostrates the polymorphism
'''

def print_area(shape):
    shape.area()


rectangle = Rectangle(4,5)
circle = Circle(6)

print_area(rectangle)
print_area(circle)


'''
Abstract Base class
polymorphism with Abstract Base class
Abstract Base Classes (ABCs) are used to define common methods for a group of related objects. 
They can enforce that derived classes implement particular methods, 
promoting consistency across different implementations.
'''

from abc import ABC,abstractmethod

# define an abstract class
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self) -> str:
        pass


class Car(Vehicle):
    def start_engine(self):
        return 'Car Engine Started'


class MotorCycle(Vehicle):
    def start_engine(self):
        return 'MotoCycle Engine Started'


# function that demonstrates polymorphism
def start_vehile(vehicle):
    print(vehicle.start_engine())


car = Car()
motorCycle = MotorCycle()

start_vehile(car)
start_vehile(motorCycle)