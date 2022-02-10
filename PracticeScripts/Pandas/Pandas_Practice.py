import pandas as pd

path = "C:\\Users\\320052425\\Desktop\\USTTraining\\PracticeScripts\\Files\\Employee_List.xlsx"

def read_excel():
    print(pd.read_excel(path,index_col=0))
    # Based on the value give for index_col, the respective column from the sheet is printed first

def print_name_sorted(columnName):
    """
    To print the data in alphabetical order of the column name
    :param columnName:
    :return:
    """
    df = pd.read_excel(path)
    sort = df.sort_values(columnName)
    print(sort)

def print_unque_data():
    """
    To print data by removing the duplicates
    :return:
    """

    df = pd.read_excel(path)
    unique = df.drop_duplicates(subset = ['first_name'],keep='first')
    # This command dropped all the duplicates in the 'first_name' columns so they are all now unique, and chose to keep the first row it found
    print(unique)

print_unque_data()