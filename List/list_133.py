# Write a Python program to check if two lists have the same elements in them in same order or not
def compare(l1,l2):
    if len(l1)!=len(l2):
        return False
    for i in range(len(l1)):
        if l1[i]!=l2[i]:
            return False
    return True
l1=[1, 2, 3, 4, 5]
l2=[1, 2, 3, 4, 5]
l3=[1, 2, 3, 5, 4]
print(compare(l1,l2))
print(compare(l1,l3))
