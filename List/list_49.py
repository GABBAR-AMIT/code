#Write a Python program to convert a list to a list of dictionaries
name=["Black", "Red", "Maroon", "Yellow"]
code=["#000000", "#FF0000", "#800000", "#FFFF00"]
a=[]# final out put
#b={}
for i,j in zip(name,code):
    b={}
    b['name']=i
    b['code']=j
    a.append(b)
print(a)