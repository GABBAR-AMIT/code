# Write a Python program to filter a list of integers using Lambda
a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

e=list(filter(lambda x: (x%2 == 0),a)) # even
print(e)
f=list(filter(lambda x: (x%2 !=0),a)) # odd
print(f)
