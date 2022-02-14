from PracticeScripts.StudentManagement.DB_Operations import ConnectToDB
from PracticeScripts.StudentManagement.ReusableMethods import ReusableMethods



class StudentSignUp:

    def student_signup(self):
        """
         To accept details of the student and create record in the DB for each student.
        :return:
        """
        print("\n")
        print("***********  WELCOME TO STUDENT SIGNUP PAGE ************")
        f_name = input("Enter your First Name: ")
        l_name = input("Enter your Last Name: ")
        reuse_methods = ReusableMethods()
        email = reuse_methods.accept_validate_email()
        u_name = ""
        pwd = reuse_methods.accept_and_validate("password")
        check = True
        while check:
            u_name = reuse_methods.accept_and_validate("username")
            db1 = ConnectToDB.cursors.execute("select * from student_details where username=\'" + u_name + "\'")
            try:
                ConnectToDB.cursors.fetchone()[0]
                print("Username exists, Please try again!")
            except:
                check = False
        sql = "insert into student_details(fname, lname, email_id, username, password) values (%s, %s, %s, %s, %s)"
        val = (f_name, l_name, email, u_name, pwd)
        try:
            pass
            dbs1 = ConnectToDB.cursors.execute(sql, val)
            ConnectToDB.myconnection.commit()
            print("Details are added successfully")
        except Exception as e:
            print(Exception)
            print(e)
            ConnectToDB.myconnection.rollback()


#tests = StudentSignUp()
#tests.student_signup()
