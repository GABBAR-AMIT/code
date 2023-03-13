# Write a Python program to get the frequency of elements in a list.
list=[1,2,3,4,5,6,6,8,8,9,9,9,7,3,2,1]
d={}
for i in list:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

for key,value in d.items():
    print(key,":",value)


