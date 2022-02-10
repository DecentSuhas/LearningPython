import mysql.connector

myconn = mysql.connector.connect(host ="localhost",user ="root",passwd = "root")
cur = myconn.cursor()

try:
    cur.execute("create database testdb")
    dbs = cur.execute("show databases")
except:
    myconn.rollback()

for x in cur:
    print(x)
myconn.close()