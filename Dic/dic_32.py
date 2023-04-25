# Write a Python program to print a dictionary line by line.
a={'Aex':{'class':'V',
        'rolld_id':2},
        'Puja':{'class':'V',
        'roll_id':3}}
for i in a:
    for j in a[i]:
        print(j,':',a[i][j])