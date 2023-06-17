
a=[10,20,30,40]
element_find=20
for i in range (len(a)):
    if a[i]==element_find:
        print(i)
        
        

def binary_search(lst,find):
    low=0
    high=len(lst)-1
    
    while low<= high:
        mid=(low+high)//2
        if lst[mid]==find:
            return mid
        elif lst[mid]<find:
            low=mid+1
        else:
            high=mid-1
    return -1

lst=[1,2,3,4,5,6,7,8,9]
find=