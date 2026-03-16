'''
A company maintains an employee management system where each employee has:
Employee ID
Name
Department
Salary

'''

# Create a dictionary to store employee details
employees = {
    101: {"name": "Ravi", "dept": "IT", "salary": 50000},
    102: {"name": "Anu", "dept": "HR", "salary": 45000},
    103: {"name": "John", "dept": "Finance", "salary": 55000}
}

#2. Access Employee Information
employee_id = 102
if employee_id in employees:
    print(f"Employee ID: {employee_id}")
    print(f"Name: {employees[employee_id]['name']}")
    print(f"Department: {employees[employee_id]['dept']}")
    print(f"Salary: {employees[employee_id]['salary']}")
else:
    print(f"Employee with ID {employee_id} not found.")

#3. Add New Employee (direct assignment)
new_employee_id = 104
new_employee_details = {"name": "Sara", "dept": "Marketing", "salary": 48000}
employees[new_employee_id] = new_employee_details
print(f"Added new employee with ID {new_employee_id}: {employees[new_employee_id]}")

#4. Update Employee Salary (update() method)
employee_id_to_update = 101
new_salary = 52000
if employee_id_to_update in employees:
    employees[employee_id_to_update].update({"salary": new_salary})
    print(f"Updated salary for employee ID {employee_id_to_update}: {employees[employee_id_to_update]['salary']}")
else:
    print(f"Employee with ID {employee_id_to_update} not found.")
    