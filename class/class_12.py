# Write a Python class named Student with two instances student1, student2 
# and assign values to the instances' attributes. Print all the attributes of 
# the student1, student2 instances with their values in the given format
class Student:
    def __init__(self, student_id, student_name, student_class):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class
        
# Initialize the two Student instances
student1 = Student(123456, "John", "YEAR 10")
student2 = Student(234567, "Jane", "YEAR 11")

# Print all the attributes of student1 in the given format
print(f"Student ID: {student1.student_id}")
print(f"Student Name: {student1.student_name}")
print(f"Student Class: {student1.student_class}")
    
# Print all the attributes of student2 in the given format
print(f"Student ID: {student2.student_id}")
print(f"Student Name: {student2.student_name}")
print(f"Student Class: {student2.student_class}")
