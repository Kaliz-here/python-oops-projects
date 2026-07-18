# Employee Management System
class Employee:
    def __init__(self, id, name, salary):
        self.name = name
        if salary <= 0 or id <= 0:
            raise ValueError("Enter valid input..!")
        else:
            self.id = id
            self.salary = salary
        
    def yearly_salary(self):
        return self.salary * 12
    
    def increment_salary(self, percentage):
        if percentage <= 0:
            raise ValueError("invalid hike..!")
        else:
            after_hike = self.salary * percentage / 100
            self.salary = after_hike + self.salary
            return self.salary
        
    def __str__(self):
        details = f"\nID : {self.id}\n"
        details += f"Name : {self.name}\n"
        details += f"Salary : {self.salary}"
        return details

class Manager(Employee):
    def __init__(self, id, name, salary, department):
        super().__init__(id, name, salary)
        self.department = department

    def __str__(self):
        details = super().__str__()
        details += f"\nDepartment : {self.department}"
        return details


total_manager = int(input("Enter Total Managers :> "))
employee_objects = [] 
employee_details = {}

# add manager in list in dict in object
for _ in range(1, total_manager + 1):
    em_name = input("\nEnter Name :> ")
    emp_id = int(input("Enter ID :> "))
    emp_salary = int(input("Enter Salary :> "))
    emp_department = input("Enter Department :> ")

    manager = Manager(emp_id, em_name, emp_salary, emp_department)
    employee_objects.append(manager)
    employee_details[emp_id] = manager

highest_salary = employee_objects[0]
lowest_salary = employee_objects[0]

# Find highest salary of manager
for highest in employee_objects:
    if highest.salary > highest_salary.salary:
        highest_salary = highest

print(f"\n| The highest Salary Of Manager |")
print(highest_salary)

# Find lowest salary of manager
for lowest in employee_objects:
    if lowest.salary < lowest_salary.salary:
        lowest_salary = lowest

print(f"\n| The Lowest Salary Of Manager |")
print(lowest_salary)

#find manager using manager ID 
find_manager = int(input("\nEnter Manager ID : "))
if find_manager in employee_details:
    print("\n| Manager found |")
    print(employee_details[find_manager])

else:
    print("| Manager not found |")

