import random

from PracticeScripts.StudentManagement.AdminLogin import AdminLogin
from PracticeScripts.StudentManagement.DB_Operations import ConnectToDB
import pandas as pd
from matplotlib import pyplot as plt


def export_students_details(tablename,u_name):
    """
    To fetch all the records from DB and write it into excel file.
    :param tablename:
    :return:
    """
    db = ConnectToDB()
    fileName = "Students_Details.xlsx"
    try:
        admin = AdminLogin()
        if admin.verify_login("admin_credentials",u_name):
            dbs1 = ConnectToDB.cursors.execute("select * from " + tablename)
            value = ConnectToDB.cursors.fetchall()
            df = pd.DataFrame(value)
            df.columns = ['First name', 'Last name', 'Email', 'Username', 'Password']
            writer = pd.ExcelWriter(fileName, engine='xlsxwriter')
            df.to_excel(writer, sheet_name='Sheet1', index=False)
            writer.save()
            print("Details exported to .xlsx file successfully")
        else:
            print("Failed to export")
    except Exception as e:
        print(e)
        ConnectToDB.myconnection.rollback()

def export_students_records(tablename,u_name):
    """
    To fetch all the records from DB and write it into excel file.
    :param tablename:
    :return:
    """
    db = ConnectToDB()
    fileName = "Students_Record.xlsx"
    try:
        admin = AdminLogin()
        if admin.verify_login("admin_credentials",u_name):
            dbs1 = ConnectToDB.cursors.execute("select * from " + tablename)
            value = ConnectToDB.cursors.fetchall()
            df = pd.DataFrame(value)
            df.columns = ['Name', 'Class', 'Section', 'ID']
            writer = pd.ExcelWriter(fileName, engine='xlsxwriter')
            df.to_excel(writer, sheet_name='Sheet1', index=False)
            writer.save()
            print("Details exported to .xlsx file successfully")
        else:
            print("Failed to export")
    except Exception as e:
        print(e)
        ConnectToDB.myconnection.rollback()


def generate_barGraph_StudentsCount():
    """
     This function generates the bar graph as per the number of students in each class
    :return:
    """
    class_9 = filter_pandas("Class",9,"filter.Class")
    class_10 = filter_pandas("Class", 10, "filter.Class")
    class_11 = filter_pandas("Class", 11, "filter.Class")
    class_12 = filter_pandas("Class", 12, "filter.Class")
    data = {'9th': class_9,'10th': class_10, '11th': class_11, '12th': class_12}
    classrooms = list(data.keys())
    values = list(data.values())
    fig = plt.figure(figsize=(10, 5))
    plots = plt.bar(classrooms, values, color='green', width=0.3)
    plt.xlabel("Class")
    plt.ylabel("No. of students admitted")
    plt.title("Students count as per class")
    plt.plot(kind="bar")
    plt.show()



def filter_pandas(columnName,classRoom,column):
    """
        This method refers the current .xlsx file and filters the data based on the class room and returns the total count
    :param columnName:
    :param classRoom:
    :param column:
    :return: total count of records/rows
    """
    df = pd.read_excel("Students_Record.xlsx")
    filter = df[df[columnName] == classRoom]  # Filter based on the column name
    value = eval(column) # Get only the column "Class" values also the passed string is converted to object so that dataframe accepts
    row_count = value.shape[0]   # Got the row count
    return row_count


#export_students_records("student_records","admin")
#generate_barGraph_StudentsCount()