#  Write a Python program to check whether any word in a given
# string contains duplicate characters or not. 
# Return True or False
a=input("enter a string:")
for i in a.split():
    if len(set(i)) != len(i):
        print("true")
        break
else:
    print("false")
