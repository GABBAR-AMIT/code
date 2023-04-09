# Write a Python program to count the number of groups of non-zero numbers separated by zeros in a given list of numbers.
# declaring the original list
lst = [3, 4, 6, 2, 0, 0, 0, 0, 0, 0, 6, 7, 6, 9, 10, 0, 0, 0, 0, 0, 5, 9, 9, 7, 4, 4, 0, 0, 0, 0, 0, 0, 5, 3, 2, 9, 7, 1]
count = 0
prev = 0
for i in lst:
    if i != 0 and prev == 0:
        count += 1
    prev = i
print(count)
