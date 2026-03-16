from collections import namedtuple

Student = namedtuple('Student', ['name', 'age', 'grade'])

s1 = Student('Ravi', 21, 'A')
s2 = Student('Priya', 22, 'B')

print(s1.name)
print(s1.age)
print(s1.grade)
print(s2)
