class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


    def display_employee(self):
        print(f"Name : {self.name}")
        print(f"Salary : {self.salary}")

employee_1 = Employee("Rahul Tiwari", 170000)
employee_1.display_employee()