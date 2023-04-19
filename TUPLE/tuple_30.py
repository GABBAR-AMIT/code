# Write a Python program to check if a specified 
# element appears in a tuple of tuples.
def check(a,ele):
    for i in a:
        if ele in i:
            return True
    return False
a=(('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
ele='Red'
if check(a,ele):
    print(ele,a)
else:
    print(ele,a)