# Write a Python program to iterate over two lists simultaneously
list1=[1,2,3,4]
list2=['one','two','three','four']
for x,y in zip(list1,list2):
    print(x,y)
