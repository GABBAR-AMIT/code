#  Write a Python program to count integers in a given mixed list. 
a=['apple', 3, 'banana', 7, 10, 'orange', 'watermelon', 15, 20]
count=0
for i in a:
    if isinstance(i,int):
        count+=1
print(count)