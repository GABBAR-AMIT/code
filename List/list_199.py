# Write a Python program to convert a Unicode list to a list of strings
a=['\u0048', '\u0065', '\u006c', '\u006c', '\u006f']
b=[str(i) for i in a]
print(b)