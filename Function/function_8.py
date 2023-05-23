# Write a Python function that takes a list and returns a new list with distinct elements 
# from the first list.
#Sample List : [1,2,3,3,3,3,4,5]
#Unique List : [1, 2, 3, 4, 5]
def unique_list(a):
    x=[]
    for i in a:
        if i not in x:
            x.append(i)
    return x
print(unique_list([9,8,7,7,7,6,5,4,3,2,1]))
