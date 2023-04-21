# Write a Python script to check whether a given key already exists in a dictionary
a={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def key(dic):
    if dic in a:
        return True
    else:
        return False
print (key(5))
print(key(90))