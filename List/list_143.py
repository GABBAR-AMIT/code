#  Write a Python program to get the frequency of elements in a given list of lists.
def count(lst):
    l={}
    for i in lst:
        for j in i:
            if j in l:
                l[j]+=1
            else:
                l[j]=1
    return l
lst=[[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]
l=count(lst)
print(l)