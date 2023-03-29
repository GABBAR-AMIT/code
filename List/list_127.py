# Write a Python program to remove words from a given list of strings containing 
# a character or string.
list1=['Red color', 'Orange#', 'Green', 'Orange @', 'White']
list3=[]
for i in list1:
    b = i.split(" ")
    list3+=b
list2=['#', 'color', '@']
print(list3)
for i in list2:
    for j in list3:
        if i in j:
            list3.remove(j)
print(list3)