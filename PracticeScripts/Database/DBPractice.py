import mysql.connector


class ConnectToDB:
    # Assuming 'himalayadb' database is already created
    myconnection = mysql.connector.connect(host="localhost", user="root", password="root", database="himalayadb")
    cursors = myconnection.cursor()

    def createDB(self, dbname):
        try:
            ConnectToDB.cursors.execute("create database "+dbname)
        except:
            ConnectToDB.myconnection.rollback()

    def display_DBs(self):

        dbs = ConnectToDB.cursors.execute("show databases")
        for x in ConnectToDB.cursors:
            print(x)
        ConnectToDB.myconnection.close()

    def createTable(self, tablename):

        try:
            dbs1 = ConnectToDB.cursors.execute(
                "create table " + tablename + "(product_name varchar(20) not null, price int not null primary key, validity int not null)")
            dbs2 = ConnectToDB.cursors.execute("show tables")
        except:
            ConnectToDB.myconnection.rollback()


    def display_tables(self):
        try:
            dbs = ConnectToDB.cursors.execute("show tables")
            for x in ConnectToDB.cursors:
                print(x)
        except:
            ConnectToDB.myconnection.rollback()

    def deleteTable(self, tablename):
        try:
            db = ConnectToDB.cursors.execute("Drop table " + tablename)
        except:
            ConnectToDB.myconnection.rollback()

    def insert_into_table(self,tablename):

        """ With user input """

        product_name = input("Enter the product name: ")
        product_price = int(input("Enter the product price: "))
        product_validity = int(input("Enter the validity: "))
        sql = "insert into "+tablename+"(product_name, price, validity) values (%s,%s,%s)"
        val = (product_name, product_price, product_validity)
        try:
            dbs1 = ConnectToDB.cursors.execute(sql, val)
            ConnectToDB.myconnection.commit()
        except:
            ConnectToDB.myconnection.rollback()

    def display_records(self, tablename):
        try:
            dbs1 = ConnectToDB.cursors.execute("select * from "+tablename)
            rowCount = dbs1.rowcount
            print("RowCount: ",rowCount)
            for x in ConnectToDB.cursors:
                print(x)
        except:
            ConnectToDB.myconnection.rollback()

    def display_single_record(self, param):
        try:
            db = ConnectToDB.cursors.execute("select * from product_details where product_name=\'" + param + "\'")
            if ConnectToDB.cursors.fetchone()[0]:
                print("Value exists")
            else:
                print("Doesnt exist")
            # for x in ConnectToDB.cursors:
            #     print(x)
        except:
            ConnectToDB.myconnection.rollback()

    def verifyRecord(self, tablename):
        param = ""
        try:
            check = True
            while check:
                param = input("Enter product name: ")
                db = ConnectToDB.cursors.execute("select * from product_details where product_name=\'" + param + "\'")
                try:
                    ConnectToDB.cursors.fetchone()[0]
                    print("Username exists, Please try again!")
                except:
                    print("Username is unique")
                    print(param)
                    check = False
        except Exception as e:
            print(e)
            ConnectToDB.myconnection.rollback()


test1 = ConnectToDB()
test1.verifyRecord("product_details")
