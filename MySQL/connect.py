import mysql.connector as myconn

mydb=myconn.connect(host="localhost",user="root",password="19051998")
print(mydb,"connection establised....")