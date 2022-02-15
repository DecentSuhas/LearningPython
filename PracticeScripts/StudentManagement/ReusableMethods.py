import re


class ReusableMethods:

    def accept_and_validate(self, fieldName):
        """
        Accept the user input
        This method can be used for username/password as input
        Input should meet conditions
        Length should be equal to more than 6
        Should contain [a-b],[A-B],0-9,[any one special character]
        :param: fieldName
        :return string:
        """
        flag = 0
        password_error_msg = '''
        Must include minimum 6 characters, 1 capital letter, 1 small letter, 1 number,
        symbols \'_ @\' and space is not allowed
        '''
        while flag <= 0:
            user_input = input("Enter the valid " + fieldName + ": ")
            if ((fieldName.lower() == "password" or fieldName.upper() == "PASSWORD")) and (len(user_input) < 6):
                flag = -1
                print(password_error_msg)
            elif ((fieldName.lower() == "username" or fieldName.upper() == "USERNAME")) and (len(user_input) < 6):
                flag = -1
                print("Must be minimum 6 characters")
            elif ((fieldName.lower() == "password" or fieldName.upper() == "PASSWORD")) and not (
            re.search("[A-Z]", user_input)):
                flag = -1
                print(password_error_msg)
            elif not re.search("[a-z]", user_input):
                flag = -1
                print(password_error_msg)
            elif ((fieldName.lower() == "password" or fieldName.upper() == "PASSWORD")) and not (
            re.search("[0-9]", user_input)):
                flag = -1
                print(password_error_msg)
            elif ((fieldName.lower() == "password" or fieldName.upper() == "PASSWORD")) and not (
            re.search("[_@]", user_input)):
                flag = -1
                print(password_error_msg)
            elif ((fieldName.lower() == "username" or fieldName.upper() == "username")) and re.search(
                    "[ #*!$@^&+=~`><?:;|,/]", user_input):
                flag = -1
                print("Space and no special symbols other than \'_\' is allowed")
            elif ((fieldName.lower() == "password" or fieldName.upper() == "password")) and re.search(
                    "[ #*!$^&+=~`><?:;|,/]", user_input):
                flag = -1
                print(password_error_msg)
            else:
                flag = 1
        return user_input

    def accept_validate_email(self):
        """
            To accept the email ID with validation.
        :return:
        """
        error_msg = "Must have minimum 7 characters, domain name. No space and invalid special characters allowed except \'_\'"
        flag = 0
        count = 0
        while flag <= 0:
            count = 0
            email = input("Please enter valid email: ")
            for i in range(len(email)):
                if email[i] == "@":
                    count = count + 1
            if (len(email) < 7):
                flag = -1
                print(error_msg)
            elif not re.search("[a-z]", email):
                flag = -1
                print(error_msg)
            elif not re.search(".com$", email):
                flag = -1
                print(error_msg)
            elif not re.search("@", email):
                flag = -1
                print(error_msg)
            elif count > 1:
                flag = -1
                print("Only 1 @ symbol is allowed")
            elif re.search("[ #*!$^&+=~`><?:;|,/]", email):
                flag = -1
                print(error_msg)
            else:
                flag = 1
        return email




