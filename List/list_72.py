#Write a Python program to flatten a given nested list structure
list=[[1, 2], [3, 4, 5], [6], [7, 8, 9, 10]]
b=[]
for i in list:
    for j in i:
        b.append(j)
print(b)
