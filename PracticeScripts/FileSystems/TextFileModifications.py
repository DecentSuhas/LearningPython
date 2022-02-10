import os


def createFile():
    """ Creates a new file"""
    file_1 = open("SampleFile.txt", "x")
    file_1.close()


def writeIntoFile():
    """ Writes in the file"""
    file_1 = open("SampleFile.txt", "w")
    file_1.write("First line written through coding")
    file_1.close()


def rewriteIntoFile():
    """ Rewrites in the file"""
    file_1 = open("SampleFile.txt", "w")
    file_1.write("ReWriting already written sentence.")
    file_1.close()


def good_practice():
    """ Always prefer to open "With" statement so that you dont need to explicitly close"""
    with open("SampleFile.txt", "r") as f:
        content = f.read(10)
    print(content)


def addTextToExisting():
    """ Adds(appends) text to existing file """
    file_1 = open("SampleFile.txt", "a")
    file_1.write(" adding to the existing line... voila")
    file_1.close()


def addTextInMultiLines():
    """ Adds(appends) texts in multi line """
    file_1 = open("SampleFile.txt", "a")
    file_1.write('''
    How does it look... yay
    ''')
    file_1.close()


def read_1():
    """ To read complete content """
    file_1 = open("SampleFile.txt", "r")
    print(file_1.read(5))
    file_1.close()


def read_2():
    """ To read complete content """
    file_1 = open("SampleFile.txt", "r")
    for i in file_1:
        print(i)
    file_1.close()


def readLine():
    """ To read the line """
    file_1 = open("SampleFile.txt", "r")
    print(file_1.readline())
    file_1.close()


def getCurrentDirectory():
    """ Gets the current directory path"""
    print(os.getcwd())


def createDirectory():
    """ It creates a new directory/folder """
    os.mkdir("C:/Users/320052425/Desktop/USTTraining/PracticeScripts/FileSystems/Testing")


def deleteDirectory():
    """ To delete the directory """
    os.rmdir("dd")


def crateFile():
    file_1 = open("TestFile.txt", "x")
    file_1.close()


def copyPaste_File():
    """ To copy the file from one location to paste in another location"""

def writeRead():
    """ It writes and then reads"""   # Note sure
    file_1 = open("TestFile.txt", "w+")
    file_1.write("Hola")
    print(file_1.read())

def write_names():
    """ Accept five sports names from the user and write in a file “sport.txt” (each name should write in separate line)"""
    file_2 = open("Names.txt","w")
    for i in range(4):
        name = input("Enter the name")
        file_2.write(name)
        file_2.writelines("\n")
    file_2.close()

def hobbies():
    """ Accept five hobbies from the user and write in a file “hobby.txt” (each hobby should write in separate line) without using write() function. """
    file2 = open("Hobbies.txt","a")
    for i in range(4):
        hobby = input("Enter the hobby: ")
        file2.write(hobby)
        file2.write(" ")
    file2.close()

hobbies()

