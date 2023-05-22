# Write a Python function to sum all the numbers in a list.
def sum (numbs):
    a=0
    for x in numbs:
        a+=x
    return a
print(sum((99,101,100)))