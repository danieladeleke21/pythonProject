import math
import re
# program to check password security

def c_pswd (pswd):
    import re

    # checking password length
    if len(pswd) >= 8 and len(pswd) <= 25:
        # checking if the password contains uppercase
        res = any(ele.isupper() for ele in pswd)
        if res is True:
            # Checking if the password contains lowercase
            res_2 = any(ele.islower() for ele in pswd)
            if res_2 is True:
                # checking for numbers
                    if any(ele.isdigit() for ele in pswd):

                        # checking for special characters
                        string_check = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
                        if (string_check.search(pswd) == None):
                            return print("Password must contain a special character")
                        else:
                            print("Correct format")
                            #Confirm password
                            confirm_pswd = input("Confirm password: ")
                            if password == confirm_pswd:
                                return print("Password confirmed")
                            else:
                                return print("Reconfirm password")

                            return print("Welcome" + " " + f_name)

                    else:
                        return print("Password must contain at least one number")
            else:
                return print("Password must contain at least one lowercase")
        return print("Password must contain at least one uppercase")
    #checking if the password is shorter that 8
    elif len(pswd) < 8:
        return print("Password must contain at least 8 characters")
    # checking if the password is more than 25
    else:
        return print("Password too long")



# Client credential input
f_name = input("First name: ")
l_name = input("Last name:")
m_name = input("Middle Name:")
email = input("Your Email:")

password = input("Input a password:")

#Calling of function
c_pswd(password)
