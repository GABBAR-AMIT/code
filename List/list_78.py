# Write a Python program to split a given list into two parts 
# where the length of the first part of the list is given
a = [1, 2, 3, 4, 5, 6,7]
length=4
first_part = a[:length]
second_part = a[length:]
print(first_part)
print(second_part)