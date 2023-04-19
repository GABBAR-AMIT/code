# Write a Python program to convert a tuple of string values 
# to a tuple of integer values
a=(('333', '33'), ('1416', '55'))
b= tuple(tuple(int(i) for i in j) for j in a)
print(b)