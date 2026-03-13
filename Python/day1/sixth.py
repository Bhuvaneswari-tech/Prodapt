#Scenario:A company HR system stores employee details. 
# Based on the employee's salary, the system must identify the salary category.

name = input("Enter Employee name: ")
salary = int(input("Enter Employee salary: "))

if salary < 25000:
    category = "Junior Level"
elif salary <= 60000:
    category = "Mid Level"
else:
    category = "Senior Level"

print(f"Employee: {name}")
print(f"Salary Type: {type(salary)}")
print(f"Category: {category}")