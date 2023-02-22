# Write a Python program to lowercase 
# the first n characters in a string.
s=input("Enter a string:")
n=int(input("Enter the number of char:"))
print(s[:n].lower() + s[n:])
