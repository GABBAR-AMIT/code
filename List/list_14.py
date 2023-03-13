#  Write a Python program to print the numbers of a specified list after removing even numbers from it.
lst = [3, 7, 11, 8, 21, 6, 2, 13]
output = []

for num in lst:
    if num % 2 !=0:
        output.append(num)
print("List with even numbers removed:",output)
