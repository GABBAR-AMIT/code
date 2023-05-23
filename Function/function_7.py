#  Write a Python function that accepts a string and counts the number of upper and lower case letters.
# Sample String : 'The quick Brow Fox'
def count(str):
    upper_count=0
    lower_count=0
    for i in str:
        if i.isupper():
            upper_count+=1
        elif i.islower():
            lower_count+=1
            return upper_count,lower_count
        
sample = 'The quick Brow Fox'
upper, lower = count(sample)
print("Uppercase count:", upper)
print("Lowercase count:", lower)