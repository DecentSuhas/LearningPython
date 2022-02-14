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
        """
        To create a particular table
        :param tablename:
        :return:
        """
        try:
            dbs1 = ConnectToDB.cursors.execute(
                "create table " + tablename + "(fname varchar(20) not null,lname varchar(10) not null, email_id varchar(10) not null primary key, username varchar(10) not null, password varchar(10) not null)")

        except:
            ConnectToDB.myconnection.rollback()

    def deleteTable(self, tablename):
        """
            To delete a particular table
        :param tablename:
        :return:
        """
        try:
            db = ConnectToDB.cursors.execute("Drop table " + tablename)
        except:
            ConnectToDB.myconnection.rollback()

    def insert_into_table(self, tablename, u_name, pwd):
        """
        To insert the username and password.
        :param tablename:
        :param u_name:
        :param pwd:
        :return:
        """

        sql = "insert into " + tablename + "(username, password) values (%s,%s)"
        val = (u_name, pwd)
        try:
            dbs1 = ConnectToDB.cursors.execute(sql, val)
            ConnectToDB.myconnection.commit()
        except Exception as e:
            print(e)
            ConnectToDB.myconnection.rollback()

    def insert_into_StudentDetails(self, tablename, f_name, l_name, e_id, u_name, p_wd):
        """
         To insert the personal details of the student based on the parameters given
        :param tablename:
        :param f_name:
        :param l_name:
        :param e_id:
        :param u_name:
        :param p_wd:
        :return:
        """
        sql = "insert into " + tablename + "(fname, lname, email_id, username, password) values (%s, %s, %s, %s, %s)"
        val = (f_name, l_name, e_id, u_name, p_wd)
        try:
            dbs1 = ConnectToDB.cursors.execute(sql, val)
            ConnectToDB.myconnection.commit()
        except Exception as e:
            print(e)
            ConnectToDB.myconnection.rollback()

    def insert_into_StudentRecords(self, tablename, s_name, classRoom, section, id):
        """
            To insert the details of the student based on the parameter given
        :param tablename:
        :param s_name:
        :param classRoom:
        :param section:
        :param id:
        :return:
        """
        sql = "insert into " + tablename + "(name, class, section, id) values (%s, %s, %s, %s)"
        val = (s_name, classRoom, section, id)
        try:
            dbs1 = ConnectToDB.cursors.execute(sql, val)
            ConnectToDB.myconnection.commit()
        except Exception as e:
            print(e)
            ConnectToDB.myconnection.rollback()

    def display_all_records(self, tablename):
        """
         To display all the rows present in a given table
        :param tablename:
        :return:
        """
        try:
            dbs1 = ConnectToDB.cursors.execute("select * from "+tablename)
            for x in ConnectToDB.cursors:
                print(x)
        except:
            ConnectToDB.myconnection.rollback()

    def display_record_of_user(self, tablename, param):
        """
         To fetch the details of a particular user
        :param tablename:
        :param param:
        :return:
        """
        try:
            #param = input("Enter the username: ")
            dbs1 = ConnectToDB.cursors.execute("select * from "+tablename+" where username="+"\'" + param + "\'")
            for x in ConnectToDB.cursors:
                print(x)
        except:
            ConnectToDB.myconnection.rollback()

    def display_record(self, query):
        """
            To fetch the particular value based on the input sql query.
        :param query:
        :return: String
        """
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

