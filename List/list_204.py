#  Write a Python program to check if the first digit or character of each element in a list is 
# the same
a=[1234, 122, 1984, 19372, 100]
n=input(': ')
for i in a:
    if str(i)[0]== n:
        print("True")
    else:
        print("False")