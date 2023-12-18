import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",passwd="")
print(mydb)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE mydb")
mycursor.execute("SHOW DATABASES")

for i in mycursor:
    print(i)