# Write a Python class named Student with two attributes student_id, student_name.
# Add a new attribute student_class and display the entire attribute and the values
# of the class. Now remove the student_name attribute and display the entire attribute
# with values
class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
    def add_class(self, student_class):
        self.student_class = student_class
    def remove_name(self):
        del self.student_name
    def display_info(self):
        print(f"Student ID: {self.student_id}")
        if hasattr(self, 'student_name'):
            print(f"Student Name: {self.student_name}")
        if hasattr(self, 'student_class'):
            print(f"Student Class: {self.student_class}")
student = Student(123456, "John")
student.display_info()
student.add_class("YEAR 10")
student.display_info()
student.remove_name()
student.display_info()
