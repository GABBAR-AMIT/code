# Write a Python program to compute the element-wise sum of given tuples+
x = (1,2,3,4)
y = (3,5,2,1)
z = (2,2,3,1)
a=tuple(map(sum,zip(x,y,z)))
print(a)