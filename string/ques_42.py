# Write a python program to count repeated characters in a string.
s=input("This is a string :")
d={}
for i in s:
    if i in d:
        d[i]+=1
        

