import csv
filename = "Practice_csv.csv"

def creatCSVFile():
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)


def writeIntoCSV_1():
    """ To add the title name in rows """
    fields = ['First Name','Last Name','Age','Citizenship']
    with open(filename, 'w') as csvfile:
        csvWriter = csv.writer(csvfile)
        csvWriter.writerow(fields)

def writeIntoCSV_2():
    """ To add columns in csv"""
    fields = ['First Name', 'Last Name', 'Age', 'Citizenship']
    values = [['Abhay', 'Singh', '66', 'Indian'],['Catherine','Fox','30','Australian'],['Samanthu','Sangakarne','32','SriLankan']]
    with open(filename, 'w') as csvfile:
        csvWriter = csv.writer(csvfile)
        csvWriter.writerow(fields)
        csvWriter.writerows(values)


def writeIntoCSV_3():
    """ To append the values in an EXISTING csv file"""
    values = [['Rashi', 'Naik', '31', 'Indian']]
    with open(filename, 'a') as csvfile:
        csvWriter = csv.writer(csvfile)
        csvWriter.writerows(values)

def readFromCSV_1():
    """ """
    rows = []
    with open(filename,'r') as csvfile:
        csvReader = csv.reader(csvfile)
        field = next(csvReader)
        print(field)

readFromCSV_1()