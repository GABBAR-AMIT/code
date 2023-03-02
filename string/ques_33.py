# Write a Python program to print the following integers with zeros to the left 
# of the specified width.

inputString = input("Enter integers separated by commas: ")
width = int(input("Enter the width: "))
n = list(map(int, inputString.split(',')))
for i in n: 
    print('{0:0{1}d}'.format(i, width))
