# . Write a Python script to sort (ascending and descending) a dictionary by value
import _operator
a={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
b=dict(sorted(a.items(),key=lambda item: item[1]))
print(b)