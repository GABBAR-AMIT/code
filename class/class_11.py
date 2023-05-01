# Write a Python class named Student with two attributes: student_id, student_name.
# Add a new attribute: student_class. Create a function to display all attributes 
# and their values in the Student class
class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
    
    # Add a new attribute to the class
    def add_class(self, student_class):
        self.student_class = student_class
    
    # Display entire attributes and their values
    def display_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Student Name: {self.student_name}")
        if hasattr(self, 'student_class'):
            print(f"Student Class: {self.student_class}")
# Create an instance of the Student class
student = Student(123456, "John")

# Add a new attribute to the class
student.add_class("YEAR 10")

# Display entire attributes and their values
student.display_info()


