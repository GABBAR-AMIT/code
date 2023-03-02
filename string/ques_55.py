#Write a Python program to find the first repeated word in a given string
str = "Hello world ! Hello Tutor Joes"
t = set()
for txt in str.split():
	if txt in t:
	  print(txt)
    else:
	  t.add(txt)
   