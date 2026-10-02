empty_tuple = ()
print(type(empty_tuple))


empty_tuple_1 = tuple()
print(type(empty_tuple_1))


numbers = tuple([1,2,3,4,5,6])
print('numbers : ',numbers)


numbers_list = list((1,2,3,4,5,6))
print('numbers_list : ',numbers_list)


'''
Accessing tuple elements
'''
print('=====================================Accessing tuple elements=============================')
print(numbers[0])
print(numbers[-1])
print(numbers[1:])
print(numbers[::])
print(numbers[::-1])
print(numbers[::-2])
print('=====================================Accessing tuple elements=============================')



'''
tuple operations
'''
print('=====================================tuple operations=============================')

mixed_tuple = (1,"hello world" , 3.24, True)

concatenated = numbers + mixed_tuple
print('concatenated : ',concatenated)


print('mixed_tuple*3 : ',mixed_tuple*3)
print('=====================================tuple operations=============================')




'''
tuple methods
'''
print('=====================================tuple methods=============================')
print(numbers.count(1))

print(numbers.index(4))

print(mixed_tuple.index("hello world"))

print('=====================================tuple methods=============================')



'''
Nested Tuples
'''
print('=====================================Nested Tuples=============================')
nested_tuples = ((1,2,3),("a","b","c"),(True,False))
print(nested_tuples[0])
print(nested_tuples[1][2])
print('=====================================Nested Tuples=============================')



'''
Iterating the Tuples
'''
print('=====================================Iterating the Tuples=============================')

for sub_tuple in nested_tuples:
    for item in sub_tuple:
        print(item,end=" ")
    print()

print('=====================================Iterating the Tuples=============================')


'''
Immutable nature of tuples
'''
print('=====================================Immutable nature of tuples=============================')

numbers[1] = "krish"
'''
numbers[1] = "krish"
    ~~~~~~~^^^
TypeError: 'tuple' object does not support item assignment
'''
print('=====================================Immutable nature of tuples=============================')