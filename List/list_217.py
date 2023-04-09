# Write a Python program to split values into two groups, based on the result of the given filtering function.
def splite(lst,filter):
    list1=[i for i in lst if filter(i)]
    list2=[i for i in lst if not filter(i)]
    return list1,list2
lst=[1, 2, 3, 4, 5, 6]
list1,list2=splite(lst,lambda x: x%2==0)
print(list1)
print(list2)