# Write a Python program to generate groups of five consecutive numbers in a list.
list=[]
for i in range(1,16):
    if i % 5==1:
        l=[i]
    elif i % 5 !=0:
        l.append(i)
    else:
        l.append(i)
        list.append(l)
print(list)
