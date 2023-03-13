# Write a Python program to sort a list of dictionaries using Lambda.
m=[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
m.sort (key=lambda x: x['color'])
print(m)