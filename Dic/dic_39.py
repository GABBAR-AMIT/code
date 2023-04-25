# Write a Python program to store dictionary data in a JSON file.
import json
a={"students":[{"firstName": "Nikki", "lastName": "Roysden"},
               {"firstName": "Mervin", "lastName": "Friedland"},
               {"firstName": "Aron ", "lastName": "Wilkins"}],
"teachers":[{"firstName": "Amberly", "lastName": "Calico"},
         {"firstName": "Regine", "lastName": "Agtarap"}]}
with open ("dictionary", "w") as i:
    json.dump(a,i)
with open('dictionary') as i:
    d=json.load(i)
print(d)