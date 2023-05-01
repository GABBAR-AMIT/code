# Write a Python program to create a class and display the namespace of that class
class myclass:
    x=10
    def __init__(self,a,b):
        self.a=a
        self.b=b
print(myclass.__dict__)