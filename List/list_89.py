# Write a Python program to Zip two given lists of lists. Go to the editor
list1 = [[1,2,3], [4,5,6], [7,8,9]]
list2 = [['a','b'], ['c','d'], ['e','f']]
z=list(map(list.__add__,list1,list2))
print(z)