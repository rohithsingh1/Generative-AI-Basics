'''
empty dictionaries
'''

empty_dict = {}
print(type(empty_dict))

empty_dict1 = dict()
print(type(empty_dict1))


student = {"name":"rohith", "age":27,"grade":'A'}

'''
Accessing the dict elements
'''
print('=====================================Accessing the dict elements=============================')
print(student["grade"])
print(student["age"])
print(student.get('grade'))
print(student.get('last_name'))
print(student.get('last_name','Not Available'))
print('=====================================Accessing the dict elements=============================')



'''
Modifying dict elements
'''
print('=====================================Modifying dict elements=============================')
student['age'] = 14
student['address'] = 'india'
del student['grade']
print(student)
print('=====================================Modifying dict elements=============================')


'''
dict methods
'''
print('=====================================dict methods=============================')
keys = student.keys()
print(f"keys: {keys}")

values = student.values()
print(f"values : {values}")

items = student.items()
print(f"items : {items}")

student_copy = student.copy()
student['score'] = 98
print(f'student : {student}')
print(f'student_copy : {student_copy}')
print('=====================================dict methods=============================')



'''
Iterating over dict
'''
print('=====================================Iterating over dict=============================')

for key in student.keys():
    print(key,end=" ")

print(' ')

for key,value in student.items():
    print(f"{key} : {value}")

print('=====================================Iterating over dict=============================')



'''
Nested Dict
'''
print('=====================================Nested Dict=============================')

students = {
    "student1": {
        "name": "Rohit",
        "age": 20,
        "course": "Python"
    },
    "student2": {
        "name": "Amit",
        "age": 22,
        "course": "Data Science"
    }
}

print(students['student2']['course'])

for student_id,student_info in students.items():
    print(f"{student_id} : {student_info}")
    for key,value in student_info.items():
        print(f"{key} : {value}")
print('=====================================Nested Dict=============================')




'''
Dict comprehension
'''
print('=====================================Dict comprehension=============================')

squares = {x:x**2 for x in range(5)}
print(f'squares : {squares}')

even_squares = {x:x**2 for x in range(10) if x%2 == 0}
print(f'even_squares : {even_squares}')
print('=====================================Dict comprehension=============================')