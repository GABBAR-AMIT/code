# Write a Python program to convert a tuple to a string
# Define a tuple with some values
my_tuple = ('apple', 'banana', 'cherry')
string_ver = ', '.join([str(i) for i in my_tuple])
print("Tuple:", my_tuple)
print("String version:", string_ver)
