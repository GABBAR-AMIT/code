l=[87, 88, 56, 89, 44, 100, 23, 87, 1]
b=[]
for i in range(len(l)):
    for j in range(i + 1, len(l)):

        if l[i] > l[j]:
            l[i], l[j] = l[j], l[i]
print(l)
