# #!/usr/bin/python3

# import re as re

# user_password = input("Enter the password you would like to check: ")

# if(len(user_password) >= 8):
#     if(bool(re.match('((?.=*\d)(?=.*[a=z])(?.=*[A-Z])(?.=*[!@#$%^&*]).{8,30})', user_password)) == True):
#         print("Your password is strong")
#     elif(bool(re.match('((\d)([a=z]*)([A-Z]*)([!@#$%^&*]*).{8,30})', user_password)) == True):
#         print("Your password is weak!")

# else:
#     print("You have entered an invalid password!")

import re

password = input("\nEnter the password: ")
if(len(password) >= 14):
    if(bool(re.match('((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*]).{8,30})', password)) == True):
        print("\nYour password is STRONG!..........exiting\n")
    elif(bool(re.match('((\d*)([a-z]*)([A-Z]*)([!@#$%^&*]*).{8,30})', password)) == True):
        print("\nYour password is WEAK!........exiting\n")
else:
    print("\nYou have entered an invalid password.........exiting\n")
