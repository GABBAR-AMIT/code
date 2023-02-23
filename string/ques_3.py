#  Write a Python program to get a string made of the first 2 
# and last 2 characters of a given string. If the string length
# is lessthan 2, return the empty string instead

input = input("Enter a string: ")
output = input[:2] + input[-2:] if len(input) >= 2 else ''

print("Output string: " + output)

