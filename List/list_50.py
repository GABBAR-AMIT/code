# Write a Python program to sort a list of nested dictionaries
a=[{"key": { 
    "subkey1":1, "subkey2":"a"  
    }},
   {"key": { 
       "subkey1":10, "subkey2":"b" 
       }},
{"key":{ 
    "subkey1":5, "subkey2":"c" 
    }}]
a.sort(key=lambda e:e['key']['subkey1'])
print(a)