# Write a Python program to find the first even and odd number in a given list of numbers
def numlist(lst):
    even=None
    odd=None
    for i in lst:
        if i % 2==0 and even is None:
            even=i
        elif i % 2 !=0 and odd is None:
            odd=i
        if even is not None and odd is not None:
            break
    print('even number:',even)
    print(odd)
lst=[1, 3, 5, 7, 4, 1, 6, 8]
numlist(lst)
