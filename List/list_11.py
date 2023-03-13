# Write a Python function that takes two lists and returns True if they have at least one common member
a=input("Entre the number :").split(',')
b=input('enter the nth :').split(',')
c=[]
for i in a :
    for d in b:
       if i==d:
            c.append(i)
print(c)
        