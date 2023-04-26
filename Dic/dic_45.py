#  Write a Python program to verify that all values in a dictionary are the same
a={'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
if len(set(a.values()))==12:
    print("All values in the dictionary are the same.")
else:
    print("Values in the dictionary are not the same.")