#  Write a Python program to remove all elements from a given list that are present in another list.
list1 = [1, 2, 3, 4, 5,6,7,8,9,10]
list2 = [2, 4, 6,8]
new=[i for i in list1 if i not in list2]
print(new)
