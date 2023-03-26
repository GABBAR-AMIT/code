# Write a Python program to move all zero digits to the end of a given list of numbers.
a = [3,4,0,0,0,6,2,0,6,7,6,0,0,0,9,10,7,4,4,5,3,0,0,2,9,7,1]
b=[x for x in a if x!=0]
c=[x for x in a if x==0]
new=b+c
print(new)
