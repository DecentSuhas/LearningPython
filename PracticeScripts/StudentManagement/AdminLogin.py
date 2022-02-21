from PracticeScripts.StudentManagement.DB_Operations import ConnectToDB


class AdminLogin(ConnectToDB):

    def verify_login(self, tablename, u_name, db=ConnectToDB()):
        """
            To verify the sercure login by validating the credentials given
        :param tablename:
        :param u_name:
        :param db:
        :return:
        """
        query = "select password from " + tablename + " where username =\'" + u_name + "\'"
        fetch_password = db.display_record(query)
        count = 0
        for i in range(3):
            pwd = input("Enter the password: ")
            if pwd == fetch_password:
                print("Login is successful")
                return True
                break
            else:
                print("Incorrect password please try again")
                count = count + i
                if count > 2:
                    print("You have exceeded the limit. Try again later")
                    return False

    def add_student_record(self,tablename,u_name):
        """
         To create a new record of a student by the admin based on the input provided
        :param tablename:
        :param u_name:
        :return:
        """
        if self.verify_login(tablename,u_name):
            print("")
            print(" ===============  Welcome to \'ADD STUDENT RECORD PAGE\'   =============== ")
            for i in range(2):
                s_name = input("Enter student name: ")
                s_class = input("Enter class room: ")
                s_section = input("Enter section: ")
                s_id = input("Enter the id: ")
                sql_query = "insert into student_records(name, class, section, id) values (%s, %s, %s, %s)"
                sql_value = (s_name, s_class, s_section, s_id)
                try:
                    dbs1 = ConnectToDB.cursors.execute(sql_query, sql_value)
                    ConnectToDB.myconnection.commit()
                except Exception as e:
                    print(e)
                    ConnectToDB.myconnection.rollback()
        else:
            print("Login is unsuccessful")

    def get_all_records(self,tablename,db=ConnectToDB()):
        print("---------- Displaying all the records ------------")
        db.display_all_records(tablename)


#tests = AdminLogin()
#tests.verify_login("admin_credentials","admin")
#tests.add_student_record("admin_credentials","admin")
#tests.get_all_records("student_details")
#tests.get_all_records("student_records")