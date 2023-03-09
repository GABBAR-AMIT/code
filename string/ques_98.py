# Write a Python program to decapitalize the
# first letter of a given string.
import re
a=input("enter a string :")
for i in a :
    if i in a:
        re.search("[A-Z]",a)
print(a.lower())
