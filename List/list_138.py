# Write a Python program to sort a given mixed list of integers and strings.
# Numbers must be sorted before strings
a=[19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
num=[]
st=[]
for i in a:
    if isinstance(i,int):
        num.append(i)
    elif isinstance(i,str):
        st.append(i)
num.sort()
st.sort()
b=num+st
print(b)