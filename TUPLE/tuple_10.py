#  Write a Python program to check whether an element exists within a tuple
# Define a tuple with some values
my_tuple = (1, 2, 3, 4, 5)
element = 3
if element in my_tuple:
    print(element, "exists in", my_tuple)
else:
    print(element, "does not exist in", my_tuple)
