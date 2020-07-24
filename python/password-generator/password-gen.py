#!/usr/bin/python3

import random
import string


def get_rand_passwd(length):

    try:
        user_input = int(input("""

Please choose the number for your desired password type:
    
    1) Alpha
    2) Numeric
    3) Alphanumeric

input: """))

        if user_input == 1:
            password_characters_string = string.ascii_letters
            password = ''.join(random.choice(password_characters_string)
                               for i in range(length))
            print("\nYour PASSWORD is: ", password + "\n")

        elif user_input == 2:
            password_characters_string = string.digits
            password = ''.join(random.choice(password_characters_string)
                               for i in range(length))
            print("\nYour PASSWORD is: ", password + "\n")

        elif user_input == 3:
            password_characters_string = string.ascii_letters + \
                string.digits + string.punctuation
            password = ''.join(random.choice(password_characters_string)
                               for i in range(length))
            print("\nYour PASSWORD is: ", password + "\n")

        else:
            print("\nThat is not a valid digit.........exiting\n")

    except ValueError:
        print("\nUnkown Value Type..........exiting\n")


get_rand_passwd(16)
