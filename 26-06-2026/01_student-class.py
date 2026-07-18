class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")

student_1 = Student("Manav", 20)
student_1.display_info()