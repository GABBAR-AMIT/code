#  Write a Python program to count Uppercase, Lowercase, special characters and numeric values in a given string
a=input('Enter a string:')
lower=0
upper=0
special=0
numeric=0
for i in a:
    if i.isupper():
        upper=+1
    elif i.islower():
        lower=+1
    elif i.isnumeric():
        numeric=+1
    else:
        special=+1
print(lower)
print(upper)
print(special)
print(numeric)