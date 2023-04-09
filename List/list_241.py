# Write a Python program to create a dictionary with the unique values of a given list as keys and their frequencies as values.
def freq_dict(lst):
    freq = {}
    for i in lst:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq

lst = [1, 2, 3, 2, 1, 3, 4, 5, 6, 5, 4, 7, 8, 9, 8, 7, 6]
freq = freq_dict(lst)
print(freq)
