# 53. Write a Python program to find the first repeated 
# character in a given string.

a=input("the string :")
count=0
for i in a:
    if a.count(i)==2:
        print(i)