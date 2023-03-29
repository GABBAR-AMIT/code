# Write a Python program to interleave multiple lists of the same length.
def multiple_list(list1,list2,list3):
    a=[i for j in zip(list1, list2,list3) for i in j]
    return(a)

list1=[1, 2, 3, 4, 5, 6, 7]
list2=[10, 20, 30, 40, 50, 60, 70]
list3=[100, 200, 300, 400, 500, 600, 700]
print (multiple_list(list1,list2,list3))
