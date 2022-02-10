from PracticeScripts.StudentManagement.DB_Operations import ConnectToDB


class StudentLogin(ConnectToDB):

    def studentLogin(self, tablename, u_name,db=ConnectToDB()):

        query = "select password from " + tablename + " where username =\'" + u_name + "\'"
        fetch_password = db.display_record(query)
        count = 0
        for i in range(3):
            pwd = input("Enter the password: ")
            if pwd == fetch_password:
                print("Student login successful")
                return True, u_name
                break
            else:
                print("Incorrect password please try again")
                count = count + i
                if count > 2:
                    print("You have exceeded the limit. Try again later")
                    return False

    def displayDetails(self):
        u_name = input("Enter the username: ")
        if self.studentLogin("student_details",u_name):
            self.display_record_of_user("student_details", u_name)




#tests = StudentLogin()
#tests.displayDetails()