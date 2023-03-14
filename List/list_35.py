# Write a Python program to create a list by concatenating a given list with a range from 1 to n.
mylist = ['p', 'q']
n = 4
newlist = ['{}{}'.format(x, y) for y in range(1, n+1) for x in mylist]
print(newlist)