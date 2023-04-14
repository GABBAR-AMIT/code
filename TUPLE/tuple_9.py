#  Write a Python program to find repeated items in a tuple.
my_tuple = (1, 2, 3, 2, 4, 5, 4, 6, 7, 6)
repeated = []
for i in my_tuple:
    if my_tuple.count(i) > 1 and i not in repeated:
        repeated.append(i)
print("Repeated items:", repeated)
