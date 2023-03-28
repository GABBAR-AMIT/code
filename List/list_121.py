# Write a Python program to find nested list elements that are present in another list

def abc(x,y):
    z=[]
    for i in y:
        for j in i:
            if j in x:
                z.append(j)
    return z

a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
b=[[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]
print(abc(a,b))
