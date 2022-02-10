import mysql.connector

myconn = mysql.connector.connect(host ="localhost",user ="root",password = "root",database="pythondb")

print(myconn)

cur = myconn.cursor()

print(cur)
try:
    dbs = cur.execute("select * from emp")
except:
    myconn.rollback()

for x in cur:
    print(x)
myconn.close()

print(cur)