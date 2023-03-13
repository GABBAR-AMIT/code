# Write a Python program to flatten a shallow list
list=[[1,2],[3,4],[5,6]]
s=[]
for i in list:
    for j in i:
        s.append(j)
print(s)
