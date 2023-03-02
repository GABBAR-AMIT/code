#Write a Python program to find the first non-repeating character in a given string.
a=input('user input string: ')
count=0
for i in a:
    if a.count(i)==1:
        print(i)