'''
convert a number to string in python

num = 42
text = str(num)

print(text)        # "42"
print(type(text))  # <class 'str'>


convert string to number

text = "42"
num = int(text)

print(num)        # 42
print(type(num))  # <class 'int'>

text = "19.99"
num = float(text)

print(num)        # 19.99
print(type(num))  # <class 'float'>

'''


'''
Accessing list elements
'''
fruits = ["apple", "banana", "mango", "orange", "grapes"]

# last element in the list
print(fruits[-1])

# Retrieve list elements from index 1 to last index
print(fruits[1:])


# List methods

fruits.append('orange')

fruits.insert(1,"Banana")

fruits.remove("orange")

popedElement = fruits.pop()

elementIndex = fruits.index("Banana")

elementFrequency = fruits.count("Banana")



# slicing lists

numbers = [1,2,3,4,5,6,7,8,9,10]

numbers[2:5]    # Get elements from index 2 up to index 5, excluding index 5
# Output: [3, 4, 5]

numbers[:5]     # Get elements from the start up to index 5, excluding index 5
# Output: [1, 2, 3, 4, 5]

numbers[5:]     # Get elements from index 5 to the end of the list
# Output: [6, 7, 8, 9, 10]

numbers[::2]    # Get every 2nd element from the list
# Output: [1, 3, 5, 7, 9]

numbers[::-1]   # Reverse the list
# Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

numbers[::-2]   # Reverse the list and get every 2nd element
# Output: [10, 8, 6, 4, 2]



# Iterating the Lists

for number in numbers:
    print(number)


for index,number in enumerate(numbers):
    print(f"index: {index} -- number: {number}")



# list comprehension

'''
syntax = [expression for item in iterable]
'''

list = []
for x in range(10):
    list.append(x**2)

print(list)


# similar to

list1 = [x**2 for x in range(10)]

print(list1)


words = ["river", "cloud", "table", "music", "forest", "window", "python", "garden", "planet", "coffee"]

lengths = [len(word) for word in words]

print(lengths)
