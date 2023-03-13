# Write a Python program to get unique values from a list.
a=[10,20,30,40,50,50,60,70,80,90]
unique=[]
for i in a:
    if i not in unique:
        unique.append(i)
print(unique)