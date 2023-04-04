# Write a Python program to join adjacent members of a given list. 
def join(lst):
    result=[x+y for x,y in zip(lst[::2],lst[1::2])]
    return result
lst=['1','2','3','4','5','6','7','8']
print(join(lst))
