# Write a Python program to generate a number in a specified range except 
# for some specific numbers.
from random import choice
def random(start,end,expect):
    a=choice([i for i in range(start,end)if i not in expect])
    return a
start=1
end=10
expect=[2,9,10]
print(random(start,end,expect))
