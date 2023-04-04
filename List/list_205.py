# Write a Python program to find the indices of elements in a given list that are greater than a specified value.
a=[1234, 1522, 1984, 19372, 1000, 2342, 7626]
b=[i for i in range(len(a)) if a[i]>3000]
'''for i in range(0,len(a)):
    if a[i]>3000:
        b.append(i)'''
print(b)

