
# Write a Python program to find the last occurrence of a specified item in a given list.
def last_occurrence(l1, ch):
    return ''.join(l1).rindex(ch)

chars = ['s','d','f','s','d','f','s','f','k','o','p','i','w','e','k','c']
print("Original list:")
print(chars)
ch = 'f'
print("Last occurrence of",ch,"in the said list:")
print(last_occurrence(chars, ch))

