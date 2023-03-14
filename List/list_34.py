n = int(input(" enter the number : "))
l=[]
o=[]
for i in range(2,n+1):
    if i not in l:
        o.append(i)
        for j in range(i*i, n+1, i):
            l.append(j)
print(o)