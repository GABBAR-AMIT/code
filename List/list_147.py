# Write a Python program to combine two lists into another list randomly.
import random
def combine(list1,list2):
    a=list1+list2
    random.shuffle(a)
    return a
list1=[1, 2, 7, 8, 3, 7]
list2=[4, 3, 8, 9, 4, 3, 8, 9]
b=combine(list1,list2)
print(b)
