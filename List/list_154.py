#Write a Python program to join two given list of lists of the same length, element wise
def join(lst1,lst2):
    l=[]
    for i in range(len(lst1)):
        l.append(lst1[i]+lst2[i])
    return l

lst1=[[10, 20], [30, 40], [50, 60], [30, 20, 80]]
lst2=[[61], [12, 14, 15], [12, 13, 19, 20], [12]]
result=join(lst1,lst2)
print(result)