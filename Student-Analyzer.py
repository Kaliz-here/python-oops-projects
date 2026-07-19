# Student Analyzer
class Student:
    def __init__(self, name, marks):
        self.name = name
        if(marks < 0 or marks > 100):
            raise ValueError("Invalid Marks..!")
        else:
            self.marks = marks

    def grade(self):
        if(self.marks >= 90):
            return "A"
        
        elif(self.marks >= 80 and self.marks <= 89):
            return "B"
        
        elif(self.marks >= 70 and self.marks <= 79):
            return "C"

        elif(self.marks >= 60 and self.marks <= 69):
            return "D"
        
        else:
            return "F"
        
    def __str__(self):
        return f"Name : {self.name} | Marks : {self.marks} | Grade : {self.grade()}"

student_Object = []
users_count = int(input("How Many Student : "))

for user in range(1, users_count + 1):
    student = input("Enter name : ")
    Marks = int(input("Enter Marks : "))
    print()
    student_Object.append(Student(student, Marks))

largest_temp = student_Object[0]
lowest_temp = student_Object[0]

# Find Largest Grade
for student_details in student_Object:
    if(student_details.marks > largest_temp.marks):
        largest_temp = student_details

# Find Lowest Grade
for student_details in student_Object:
    if(student_details.marks < lowest_temp.marks):
        lowest_temp = student_details

print("\t\tTOPPER")
print(largest_temp)

print("\n\t\tLOWEST")
print(lowest_temp)