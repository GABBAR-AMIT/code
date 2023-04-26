# Write a Python program to filter a dictionary based on values
a={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
b={i:j for i,j in a .items() if j>=170}
print(b)