#  Write a Python program to concatenate element-wise three given lists
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = ['X', 'Y', 'Z']
list = []

for i in range(len(list1)):
    list.append(str(list1[i]) + str(list2[i]) + str(list3[i]))

print(list)
