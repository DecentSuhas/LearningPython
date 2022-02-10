import mysql.connector

# Create the connection object
myconn = mysql.connector.connect(host="localhost", user="root", passwd="root", database="pythondb")

# creating the cursor object
cur = myconn.cursor()

try:
    # Creating a table with name Employee having four columns i.e., name, id, salary, and department id
    dbs = cur.execute(
        "create table emp(name varchar(20) not null, id int not null primary key, salary int not null)")
except:
    myconn.rollback()

myconn.close()