# Write a Python class named Student with two attributes student_name, marks.
# Modify the attribute values of the said class and print the original and
# modified values of the said attributes.
class student:
    def __init__(self,student_name, marks):
        self.student_name=student_name
        self.marks= marks
        
    def modify_marks(self,new_marks):
        old_marks=self.marks
        self.marks=new_marks
        print(f"Modified marks for {self.student_name}: {old_marks} -> {new_marks}")
student1 = student("John", 80)
print(f"Student name: {student1.student_name}, Marks: {student1.marks}")
student1.modify_marks(90)
print(f"Student name: {student1.student_name}, Marks: {student1.marks}")

