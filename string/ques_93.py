#Write a Python program to extract numbers from a given string
a=input("enter a string :")
for i in a:
    if(i.isdigit()):
        print(i)