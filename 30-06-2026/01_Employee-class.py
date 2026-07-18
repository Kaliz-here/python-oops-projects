class Employee:

    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def annual_salary(self):
        if(self.monthly_salary <= 0):
            raise ValueError("Invalid Salary")
        
        else:
            return self.monthly_salary * 12
        
    def increment_salary(self, percentage):
        return self.monthly_salary * percentage / 100
    
    def after_increment(self):
        return self.monthly_salary + self.increment_salary(10)

    def display(self):
        print(f"Name : {self.name}")
        print(f"Monthly salary : {self.monthly_salary}")

    

staff = Employee("Manav", 75000)
staff.display()
print("annual salary : ", staff.annual_salary())
print("after increment salary : ", staff.after_increment())

        
    