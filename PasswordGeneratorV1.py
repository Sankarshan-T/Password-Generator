import random
import string

def generate_password():

    characters = string.ascii_letters + string.digits
    try:
        length = int(input("Enter your password length: "))
        if length <= 0:
            print("Error: Password length must be a positive number.")     
        elif length >20:
            print("Error: Password cannot be so long.")
        else:
            password = ''.join(random.choice(characters) for _ in range(length))
            print('Here is your password: ', password)
    except ValueError:
        print("Invalid input. Please enter a number.")

generate_password()

input("Press any key to exit")