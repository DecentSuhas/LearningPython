import random
import openpyxl
from PracticeScripts.StudentManagement.DB_Operations import ConnectToDB


def write_columnName_into_file():
    db = ConnectToDB()
    list1 = db.fetch_column_names("student_details")
    num = random.randrange(1, 100)
    file = f"Students_Details_{num}.xlsx"
    print(file)
    wb = openpyxl.Workbook()
    sheet = wb.active
    for i in range(1, len(list1)):
        col = sheet.cell(row=1, column=i)
        col.value = list1[i]
    wb.save(file)


write_columnName_into_file()
