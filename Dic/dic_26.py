# Write a Python program to count the values associated with a 
# key in a dictionary.
a=[{'id': 1, 'success': True, 'name': 'Lary'},
 {'id': 2, 'success': False, 'name': 'Rabi'},
 {'id': 3, 'success': True, 'name': 'Alex'}]
print(sum(i['id'] for i in a))
print