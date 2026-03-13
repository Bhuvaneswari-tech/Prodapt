'''
Use Case 1 — Student Marks List
Scenario:A teacher records marks of students and calculates the average score.
Requirements
number of subjects is fixed to 5
Store marks in a list.
Calculate average.

'''
m1,m2,m3,m4,m5 = map(int, input("Enter marks separated by space: ").split())
average = sum([m1,m2,m3,m4,m5]) / 5
print(f"Average marks: {average}")