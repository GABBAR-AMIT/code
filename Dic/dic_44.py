# Write a Python program to filter the height and width of students,
# which are stored in a dictionary
a={'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
b={i:j for i,j in a.items() if j[0]>=6.0 and j[1]>=70}
print("\nHeight > 6ft and Weight> 70kg:")
print(b)