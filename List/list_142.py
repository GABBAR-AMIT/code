# Write a Python program to sum a specific column of a list in a given list of lists
def coloum(lst,c):
    a=sum(i[c] for i in lst)
    return a
lst=[[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]
c=0
print(coloum(lst,c))
c=1
print(coloum(lst,c))
c=3
print(coloum(lst,c))