# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
a=input('entre the elements:').split(',')
b=a[1:4]+a[6:]
print(list(b))
