# IMPORTS
#####################
import pyfiglet
from termcolor import colored

from customeroperations.customer import customer_program
from productoperations.products import products_program
from purchase.purchase import purchase_product
from getpass import getpass
# This module is used to hide the password and username for security purposes

# VARIABLES
default_username = "adminBruce"
default_password = "brucepasscode"
# MAIN PROGRAM
##########

result = pyfiglet.figlet_format("LUKU SHOP", width=180)  # creates artwork with the words]
welcome_message = """
*************************************************************************************************************************************
Welcome to Bruce Shoe store. You'll find a variety of men shoes kindly buy as many as possible cause you can never have enough shoes.
*************************************************************************************************************************************
"""
print(colored(result, "blue"))
print(colored(welcome_message, "blue"))


def disp_menu():
    print("""
Kindly select 0 to exit or the rest to execute the other operations:
    1. Customer Operations
    2. Products Operations
    3. Purchase Product
    Q. To quite the program
    """)


def authentication(username, password):
    while True:
        username = input("Enter username: ")
        password = getpass()
        print("Kindly login to proceed.")
        if username == default_username and password == default_password:
            print(colored("\nAuthentication successful!!\n", "green"))
            break
        else:
            print(colored("\nAuthentication failure!!!\n", 'red'))


while True:
    # authentication(default_username, default_password)
    disp_menu()
    user_input = input("Please choose an option:\n")
    if user_input == "1":
        customer_program()
    elif user_input == "2":
        products_program()
    elif user_input == "3":
        purchase_product()
    elif user_input.upper() == "Q":
        print("Exiting Bruce's LUKU POS system...........")
        break
    else:
        print("Please enter a valid value in the range of 0 - 3")
