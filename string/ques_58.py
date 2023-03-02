# Write a Python program to move spaces to the front of a given string
a=input('Enter a string :')
b=""
for i in a:
    if i==" ":
        b=i+b
    else:
        b+=i
print(b)