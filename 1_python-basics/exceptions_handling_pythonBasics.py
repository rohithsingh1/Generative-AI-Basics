'''
What Are Exceptions?

Exceptions are events that disrupt the normal flow of a program. 
They occur when an error is encountered during program execution. Common exceptions include:

• ZeroDivisionError: Dividing by zero.
• FileNotFoundError: File not found.
• ValueError: Invalid value.
• TypeError: Invalid type.
'''

print('==================Handling Name Error exceptions======================')
try:
    a=b
except NameError as ne:
    print(ne)

print('==================Handling Name Error exceptions======================\n')


print('==================Zero Division Error======================')

try:
    result = 1/0
except ZeroDivisionError as ze:
    print(ze)

print('==================Zero Division Error======================\n')


print('==================Multiple Exceptions example 1======================')

try:
    result = 1/2
    a=b
except ZeroDivisionError as zeroError:
    print(zeroError)
except Exception as ex:
    print(ex)

print('==================Multiple Exceptions example 1======================\n')


print('==================Multiple Exceptions example 2======================')

try:
    input_number = int(input("Enter the number"))
    result = 10/input_number
except ValueError as valErr:
    print(valErr)
    print("Please enter a valid number")
except ZeroDivisionError as zeroDivErr:
    print(zeroDivErr)
    print('enter denominator greater than 0')
except Exception as ex:
    print(ex)

print('==================Multiple Exceptions example 2======================\n')


print('==================Try,catch,else block======================')

try:
    input_number = int(input("Enter the number"))
    result = 10/input_number
except ValueError as valErr:
    print(valErr)
    print("Please enter a valid number")
except ZeroDivisionError as zeroDivErr:
    print(zeroDivErr)
    print('enter denominator greater than 0')
except Exception as ex:
    print(ex)
else:
    print(f" result : {result}")

print('==================Try,catch,else block======================\n')



print('==================Try,catch,else,finally block======================')

try:
    input_number = int(input("Enter the number"))
    result = 10/input_number
except ValueError as valErr:
    print(valErr)
    print("Please enter a valid number")
except ZeroDivisionError as zeroDivErr:
    print(zeroDivErr)
    print('enter denominator greater than 0')
except Exception as ex:
    print(ex)
else:
    print(f" result : {result}")
finally:
    print("Finall block executed")

print('==================Try,catch,else,finally block======================\n')