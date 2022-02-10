import mysql.connector

myCon = mysql.connector.connect(host = "localhost", user = "root", password="root", database="pythondb")

# Creating the cursor object
cur = myCon.cursor()
sql = "insert into emp(name, id, salary) values (%s,%s,%s)"
val = ("Abraham", 103, 10000)

# Creating a table with name Employee having four columns
dbs = cur.execute(sql, val)
myCon.commit()

for x in cur:
    print(x)
print(cur.rowcount,"records inserted")
myCon.close()