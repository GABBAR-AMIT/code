# Write a Python program to create a list reflecting 
# the run-length encoding from a given list of integers or a
# given list of characters
a=input("enter a string:")
d={}
for i in a:
    k=d.keys()
    if i in k:
        d[i]+=1
    else:
        d[i]=1
key=list(d.keys())
val=list(d.values())
l=[]
for i in 