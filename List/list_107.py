# Write a Python program to remove a specified column from a given nested list
a=[[4, 5, 6, 8],
  [2, 7, 10, 9],
  [12, 16, 18, 20]]
[i.pop(1) for i in a]
print(a)

