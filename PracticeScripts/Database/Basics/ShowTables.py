import mysql.connector

myconn = mysql.connector.connect(host ="localhost",user ="root",passwd = "root",database="pythondb")
cur = myconn.cursor()

try:
    dbs = cur.execute("show tables")
except:
    myconn.rollback()

for x in cur:
    print(x)
myconn.close()