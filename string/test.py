# Write a Python program to count the number of characters
# (character frequency) in a string.
a=input("Enter a string to count:")
d={}
for i in a:
    k=d.keys()
    if i in k:
        d[i]+=1
    else:
        d[i]=1
print(d)