#### Common Operator Overloading Magic Methods
'''
__add__(self, other): Adds two objects using the + operator.
__sub__(self, other): Subtracts two objects using the - operator.
__mul__(self, other): Multiplies two objects using the * operator.
__truediv__(self, other): Divides two objects using the / operator.
__eq__(self, other): Checks if two objects are equal using the == operator.
__lt__(self, other): Checks if one object is less than another using the < operator.

__gt__
'''

class Vector:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y

    def __add__(self, other):
        print(f"self.x = {self.x} , self.y = {self.y} , other.x = {other.x} , other.y = {other.y}")
        return Vector(self.x + other.x , self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x , self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * other.x , self.y * other.y)

    def __eq__(self, value) -> bool:
        return self.x == value.x and self.y == value.y

    def __repr__(self) -> str:
        return f"Vector({self.x} , {self.y})"


v1 = Vector(2,3)
v2 = Vector(4,5)

print(v1 + v2)
print(v1 - v2)
print(v1 * v2)
print(v1 == v2)