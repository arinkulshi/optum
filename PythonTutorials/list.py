course = [1,2,3,4]
courses = [1,2,3,4]
#0:2

print(course[0:2])

course.append(5)

print(course)

course.insert(0,2)

print(course)

#Extend

course.extend(courses)

courses.pop() #Uses as a stack or a queue



courses.reverse()

#sort does it in place

min(course)

#Index will find the index of a value


print(course.index(3))


#In


print(10 in course)



for index,c in enumerate(courses,start=1):
    print(index,c)


#Joins the values from a list
course_str = ' '.join(map(str,course))


print(course_str)


#Splits the values of a string into a list

#' '.join(courses)

#sets check intersection print(cs_courses.intersection(art_courses))
empty_set = set ()
s = {1,2,3}


myList = ['banana','orange','lemon']


if 'oranges' in myList:
    print(f'{myList} This is the list')
else:
    print('not found')