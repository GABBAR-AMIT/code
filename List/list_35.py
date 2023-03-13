# Write a Python program to create a list by concatenating a given list with a range from 1 to n.
a=input("Enter a list of number:").split()
b=int(input("enter a positive integer:"))
c=a+list(range(1,b+1))
print(c)
