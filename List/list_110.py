# Write a Python program to find the item with the most occurrences in a given list. 
a=['apple', 'banana', 'apple', 'orange', 'banana', 'pineapple', 'cherry', 'cherry', 'cherry']
b=None
c=0
for i in a:
    frequency=a.count(i)
    if frequency>c:
        c=frequency
        b=i
print(b)