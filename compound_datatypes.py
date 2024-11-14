fruits = ['apple','banana','cherry','date']
fruits.append('elderberry')
fruits.remove('banana')
print(sorted(fruits))


student = {'name':'John Doe', 'age': 25, 'major': "Computer Science"}
student['major'] = 'Electrical Engineering'
student['year'] = 'Senior'
print(student.keys())
print(student.values())

books = [
    {'title': "Atomic Habits", 'author': 'James Clear', 'year': 2018},
    {'title': "Winning the War in Your Mind", 'author': 'Craig Groeschel', 'year': 2019},
    {'title': "Meditations for Mortals", 'author': 'Oliver Burkeman', 'year': 2024}
]

print(books[1]['title'])
print(books[2]['year'])

for x in books:
    print(x['title']+' : '+x['author'])


courses = {'math':['nelson','camille','ben','nana','lala'],
           'history':['nelson','camille','ben','nana','lala'],
           'chemistry':['nelson','camille','ben','nana','lala']}
courses['math'].extend(['bilha','shalalakuy','daniel','paul john','donna'])
print(courses['math'])
del courses['history'][2]
print(courses['history'])
print(courses['chemistry'])
courses['physics'] = ['shalala','shaboy','what','the hell']
print(courses)