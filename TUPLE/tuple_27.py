#  Write a Python program to calculate the average value of the
# numbers in a given tuple of tuples.
def average(a):
    b=[sum(i)/len(i) for i in zip(*a)]
    return b

a=((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
avg=average(a)
print(avg)