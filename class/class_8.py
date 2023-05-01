#Write a Python program to create two empty classes, Student and Marks.
# Now create some instances and check whether they are instances of the
# said classes or not. Also, check whether the said classes are subclasses
# of the built-in object class or not.
class Student:
    pass

class Marks:
    pass

s1 = Student()
s2 = Student()
m1 = Marks()
m2 = Marks()

print(isinstance(s1, Student)) # True
print(isinstance(s2, Student)) # True
print(isinstance(m1, Marks))   # True
print(isinstance(m2, Marks))   # True

print(issubclass(Student, object)) # True
print(issubclass(Marks, object))   # True
