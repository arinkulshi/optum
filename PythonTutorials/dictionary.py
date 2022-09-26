student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

for key, value in student.items():
    print(key, value)

#Key
print(student['courses'])   

#values get by passing key
print(student.get('name','not_found'))

#del .pop . remove


print(student.keys())
print(student.values())
print(student.items())

for key,value in student.items():
    pass

for value in student.values():
    print(value)


for key in student.keys():
    print(key)