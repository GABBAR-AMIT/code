# Write a Python program to create set difference
setc1 = set(["green", "blue"])
setc2 = set(["blue", "yellow"])
diff=setc1.difference(setc2)
dif=setc2.difference(setc1)
print(diff)
print(dif)