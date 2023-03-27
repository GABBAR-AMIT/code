#  Write a Python program to extract the nth element from a given
# list of tuples
a=[('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
n=0
b=[i[n] for i in a]
print(b)