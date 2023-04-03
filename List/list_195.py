# Write a Python program to traverse a given list in reverse order, and print the 
# elements with the original index
lst=["red", "green", "white", "black"]
for i in reversed(lst):
    print(i)
for i,j in reversed(list(enumerate(lst))):
    print(i,j)