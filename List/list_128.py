# Write a Python program to calculate the sum of the numbers in a list 
# between the indices of a specified range
def list_range(list,range,sum):
    return sum(list[range:sum])
list=[2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12]
range=8,10
sum=29
print("list:",list)
print("range:",range)
print("sum:",sum)
