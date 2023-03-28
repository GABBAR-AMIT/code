# Write a Python program to calculate the product of the unique numbers in a given list.
def unique_product(lst):
    unique_number=set(lst)
    p=1
    for i in unique_number:
        p*=i
    return p
lst= [10, 20, 30, 40, 20, 50, 60, 40]
p=unique_product(lst)
print(p)
