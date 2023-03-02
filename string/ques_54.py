#
a=input("the string :")
d={}
y={}
for i in a:
    k=d.keys()
    if i in k :
        y[i]=a.index(i)
    else:
        d[i]=a.index(i)
print(y)