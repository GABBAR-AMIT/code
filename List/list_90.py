# Write a Python program to count the number of lists in a given list of lists.
a = [[1,2,3], ['a','b'], [True,False], [4.5, 6.7, 8.9]]

count = 0
for i in a:
    count += 1

print("Number of lists in the given list of lists:", count)
