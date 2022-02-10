import mysql.connector


class ConnectToDB:
    # Assuming 'studentmanagement' database is already created
    myconnection = mysql.connector.connect(host="localhost", user="root", password="root",
                                           database="studentmanagement")
    cursors = myconnection.cursor()

    def createDB(self, dbname):
        try:
            ConnectToDB.cursors.execute("create database " + dbname)
        except:
            ConnectToDB.myconnection.rollback()

    def createTable_adminCreds(self, tablename):

        try:
            dbs1 = ConnectToDB.cursors.execute(
                "create table " + tablename + "(username varchar(20) not null primary key, password varchar(20) not null)")
        except:
            ConnectToDB.myconnection.rollback()

    def createTable_studentRecords(self, tablename):

        try:
            dbs1 = ConnectToDB.cursors.execute(
                "create table " + tablename + "(name varchar(20) not null,class varchar(10) not null, section varchar(10) not null, id int(10) not null primary key)")
        except:
            ConnectToDB.myconnection.rollback()

    def createTable_details(self, tablename):

        try:
            dbs1 = ConnectToDB.cursors.execute(
                "create table " + tablename + "(fname varchar(20) not null,lname varchar(10) not null, email_id varchar(10) not null primary key, username varchar(10) not null, password varchar(10) not null)")

        except:
            ConnectToDB.myconnection.rollback()

    def deleteTable(self, tablename):
        try:
            db = ConnectToDB.cursors.execute("Drop table " + tablename)
        except:
            ConnectToDB.myconnection.rollback()

    def insert_into_table(self, tablename, u_name, pwd):


        sql = "insert into " + tablename + "(username, password) values (%s,%s)"
        val = (u_name, pwd)
        try:
            dbs1 = ConnectToDB.cursors.execute(sql, val)
            ConnectToDB.myconnection.commit()
        except Exception as e:
            print(e)
            ConnectToDB.myconnection.rollback()

    def insert_into_StudentDetails(self, tablename, f_name, l_name, e_id, u_name, p_wd):


        sql = "insert into " + tablename + "(fname, lname, email_id, username, password) values (%s, %s, %s, %s, %s)"
        val = (f_name, l_name, e_id, u_name, p_wd)
        try:
            dbs1 = ConnectToDB.cursors.execute(sql, val)
            ConnectToDB.myconnection.commit()
        except Exception as e:
            print(e)
            ConnectToDB.myconnection.rollback()

    def insert_into_StudentRecords(self, tablename, s_name, classRoom, section, id):


        sql = "insert into " + tablename + "(name, class, section, id) values (%s, %s, %s, %s)"
        val = (s_name, classRoom, section, id)
        try:
            dbs1 = ConnectToDB.cursors.execute(sql, val)
            ConnectToDB.myconnection.commit()
        except Exception as e:
            print(e)
            ConnectToDB.myconnection.rollback()

    def display_all_records(self, tablename):
        try:
            dbs1 = ConnectToDB.cursors.execute("select * from "+tablename)
            for x in ConnectToDB.cursors:
                print(x)
        except:
            ConnectToDB.myconnection.rollback()

    def display_record_of_user(self, tablename, param):
        try:
            #param = input("Enter the username: ")
            dbs1 = ConnectToDB.cursors.execute("select * from "+tablename+" where username="+"\'" + param + "\'")
            for x in ConnectToDB.cursors:
                print(x)
        except:
            ConnectToDB.myconnection.rollback()

    def display_record(self, query):
        try:
            dbs1 = ConnectToDB.cursors.execute(query)
            value = ConnectToDB.cursors.fetchone()
            value = value[0]
            return value
        except:
            ConnectToDB.myconnection.rollback()

#test = ConnectToDB()
#test.insert_into_StudentRecords("student_records","John","12","A", 2090)
#test.insert_into_StudentDetails("student_details","Lara","Brawn","lara.brawn@gmail.com","lara12","pass")

