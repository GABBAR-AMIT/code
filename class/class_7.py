#  Write a simple Python class named Student and display its type. Also,
# display the __dict__ attribute keys and the value of the __module__ attribute 
# of the Student class
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}"
print(type(Student))
print(dir(Student))
print(Student.__module__)
