#  Write a Python program to find the maximum and minimum values in a given list within 
# a specified index range
def max_min (lst,start,end):
    sublist=lst[start:end+1]
    mxvalue=max(sublist)
    mivalue=min(sublist)
    return(mxvalue,mivalue)
lst=[4, 3, 0, 5, 3, 0, 2, 3, 4, 2, 4, 3, 5]
start=3
end=8
result=max_min(lst,start,end)
print(result)