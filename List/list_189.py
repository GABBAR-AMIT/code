# Write a Python program to shift last element to first position and first element
# to last position in a given list
a=[1, 2, 3, 4, 5, 6, 7]
b=a[-1:]+a[1:-1]+a[:1]
print(b)
