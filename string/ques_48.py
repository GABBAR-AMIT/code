#Write a Python program to swap commas and dots in a string>
a=input('enter the float: ')
b=a.maketrans(',:.','.:,')
print(a.translate(b))