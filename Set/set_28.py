# Write a Python program to find all the unique combinations of 3 numbers 
# from a given list of numbers, adding up to a target number.
def combination(num,val):
    num=list(set(num))
    r=set()
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            com=val-num[i]-num[j]
            if com in num[:i]+num[j+1:]:
                r.add(tuple(sorted((num[i],num[j],com))))
    return list(r)
num=[1,2,3,4,5,6,7,8,9]
val=12
print(combination(num,val))