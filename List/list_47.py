# Write a Python program to insert an element before each element of a list.
a=[1,2,3,4,5,6]
inserted="a"
b=[]
for i in a:
    b.append(inserted)
    b.append(i)
print(b)