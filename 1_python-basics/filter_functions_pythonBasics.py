'''
filter function

filter even numbers
'''
print('=====================================filter even numbers=============================')

def even(num):
    if num%2 == 0:
        return True
lst = [1,2,3,4,5,6,7,8,9,10]

even_list = list(filter(even,lst))
print(f"even_list : {even_list}")
print('=====================================filter even numbers=============================')


'''
filter() to check if the age is greater than 25 in dictionaries
'''
print('=====================================filter age in dict=============================')
people=[
    {
        "name":"Rohith",
        "age":27
    },
    {
        "name":"Mahesh",
        "age":28
    },
    {
        "name":"sai",
        "age":24
    }
]

def age_greater_than_25(person):
    return person['age']>25

people_list = list(filter(age_greater_than_25,people))

print(f"people list with age > 25 : {people_list}")

print('=====================================filter age in dict=============================')