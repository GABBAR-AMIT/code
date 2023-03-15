# Write a Python program to find missing and additional 
# values in two lists
a=input('First list :').split(',')
b=input('seconf list:').split(',')
c=[]
for i in a:
    if i not in b:
        c.append(i)
print(c)
d=[]
for j in b:
    if j not in a:
        d.append(j)
print(d)