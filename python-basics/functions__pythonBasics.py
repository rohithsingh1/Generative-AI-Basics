'''
Default Parameters
'''
print('=====================================Default Parameters=============================')
def greet(name="Guest"):
    print(f"Hello {name} welcome to the paradise")

greet()
greet("Rohith")
print('=====================================Default Parameters=============================')


'''
Variable length Arguments
positional , keyword Arguments
'''
'''
Positional Arguments
'''
print('=====================================Positional Arguments=============================')

def print_numbers(*args):
    print(args) # (1, 2, 3, 4, 5, 6, 'Rohith')
    print(type(args)) # <class 'tuple'>
    for val in args:
        print(f"val : {val}")

print_numbers(1,2,3,4,5,6,"Rohith")
print('=====================================Positional Arguments=============================')


'''
Keyword Arguments
'''
print('=====================================Keyword Arguments=============================')

def print_details(**kwargs):
    print(kwargs) # {'name': 'Rohith', 'age': 27, 'country': 'india'}
    print(type(kwargs)) # <class 'dict'>
    for key,value in kwargs.items():
        print(f"{key} : {value}")

print_details(name="Rohith",age=27,country="india")
print('=====================================Keyword Arguments=============================')


'''
Positional and Keyword Arguments
'''
print('=====================================Positional and Keyword Arguments=============================')

def print_details1(*args,**kwargs):
    print(args) # (1, 2, 3, 4, 5, 6, 'Rohith')
    print(type(args)) # <class 'tuple'>
    for val in args:
        print(f"val : {val}")

    print(kwargs) # {'name': 'Rohith', 'age': 27, 'country': 'india'}
    print(type(kwargs)) # <class 'dict'>
    for key,value in kwargs.items():
        print(f"{key} : {value}")

print_details1(1,2,3,4,5,6,"Rohith",name="Rohith",age=27,country="india")

print('=====================================Positional and Keyword Arguments=============================')



def is_password_strong(password=''):
    if len(password)<8:
        return False
    obj = {
        "upperCaseCharCount":0,
        "lowerCaseCharCount":0,
        "digitCount":0,
        "specialCharCount":0,
    }
    for char in password:
        if char.isdigit():
            obj["digitCount"] += 1
        elif char.islower():
            obj["lowerCaseCharCount"] +=1
        elif char.isupper():
            obj["upperCaseCharCount"] +=1
        elif char in '!@#$_+=&*':
            obj["specialCharCount"] +=1

    for key,values in obj.items():
        if values == 0:
            return False

    return True

testCases = [
    # Valid password: has lowercase, uppercase, digit, special char, and length >= 8
    {"pwd": "Rohith@123"},

    # Invalid: missing lowercase letter
    {"pwd": "ROHITH@123"},

    # Invalid: missing uppercase letter
    {"pwd": "rohith@123"},

    # Invalid: missing digit
    {"pwd": "Rohith@abc"},

    # Invalid: missing special character
    {"pwd": "Rohith123"},

    # Invalid: length less than 8
    {"pwd": "Roh@12"},

    # Invalid: empty password
    {"pwd": ""},

    # Invalid: only lowercase
    {"pwd": "rohithabc"},

    # Invalid: only uppercase
    {"pwd": "ROHITHABC"},

    # Invalid: only digits
    {"pwd": "12345678"},

    # Invalid: only special characters
    {"pwd": "@#$%^&*!"},

    # Valid: exactly 8 characters
    {"pwd": "Ro@12345"},

    # Valid: longer strong password
    {"pwd": "Strong@Password123"},
]

for testCase in testCases:
    result = is_password_strong(testCase["pwd"])
    if result:
        print(f"{testCase['pwd']} is strong password")
    else:
        print(f"{testCase['pwd']} is weak password")




'''
The map() Function in Python

The map() function applies a given function to all items in an input list (or any other iterable) 
and returns a map object (an iterator). This is particularly useful for transforming data in a list 
comprehensively.
'''
print('=====================================The map() Function in Python=============================')
def square(x):
    return x*x

numbers = [1,2,3,4,5,6,7,8,9,10]

squaredList = list(map(square,numbers))

print(squaredList)


print('=====================================The map() Function in Python=============================')




'''
converting str numbers to int numbers in list
'''
print('=====================================converting str numbers to int numbers in list=============================')

str_numbers = ['1','2','3','4','5','6','7','8']

for index,ele in enumerate(str_numbers):
    str_numbers[index] = int(ele)

print(str_numbers)

'''
or by using map method
'''

converted_list = list(map(int,str_numbers))
print(converted_list)

print('=====================================converting str numbers to int numbers in list=============================')





print('=====================================More Map examples=============================')

words = ["apple",'banana','cherry']
upper_words = list(map(str.upper,words))
print(f"upper case words list : {upper_words}")


def get_name(person):
    return person["name"]

people=[
    {
        "name":"Rohith",
        "age":27
    },
    {
        "name":"Mahesh",
        "age":28
    }
]

person_name_list = list(map(get_name,people))
print(f"person_name_list : {person_name_list}")

print('=====================================More Map examples=============================')