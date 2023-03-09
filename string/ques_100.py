#  Write a Python program to check whether any word in a given
# string contains duplicate characters or not. 
# Return True or False
a=input("enter a string:")
d=a.split()
for i in d:
    if len (set(i))!= len(i):
        print("true")
    else:
        print("false")
print(a)
