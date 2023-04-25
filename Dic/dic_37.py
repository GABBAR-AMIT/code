# Write a Python program to replace dictionary values with their sums.
def sum (lst):
    for i in lst:
        a=i.pop('V')
        b=i.pop('VI')
        i['V+VI']=(a+b)/2
        return lst
lst=[
  {'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82},
  {'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},
  {'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}
]
print(sum(lst))