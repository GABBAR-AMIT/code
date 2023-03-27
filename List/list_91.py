#Write a Python program to find a list with maximum and minimum lengths
a=[[1,2,3,4], ['a','b'], [True,False], [4.5, 6.7, 8.9], [0], ['hello']]
b=len(max(a,key=len))
c=len(min(a,key=len))
print(b)
print(c)
