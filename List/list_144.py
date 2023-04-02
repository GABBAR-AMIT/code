# Write a Python program to extract every first or specified element from a 
# given two-dimensional list
def element(lst,index):
    l=[]
    for i in lst:
        l.append(i[index])
    return l
lst=[[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]]
a=element(lst,0)
print(a)
b=element(lst,2)
print(b)