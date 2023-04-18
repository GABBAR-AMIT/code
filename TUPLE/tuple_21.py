# Write a Python program to replace the last value of tuples in a list
a=[(10, 20, 40), (40, 50, 60), (70, 80, 90)]
for i in range(len(a)):
    tuple_to_list=list(a[i])
    tuple_to_list[-1]='100'
    a[i]=tuple(tuple_to_list)
print(a)
