# Write a Python program to find the second most repeated word in a given string
a=input('the string:')
c={}
b=a.split()
for i in b:
    if i in c:
        c[i]+=1
    else:
        c[i]=1
s=sorted(c.items())
print(s[-1])