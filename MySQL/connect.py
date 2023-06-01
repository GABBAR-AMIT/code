import mysql.connector as myconn

mydb=myconn.connect(host="localhost",user="root",password="Mysql@1080")
print(mydb,"connection establised....")