# IMPORTS
#####################
import pyfiglet
from termcolor import colored
import productoperations.products
import customeroperations.customer

# MAIN PROGRAM
##########

result = pyfiglet.figlet_format("LUKU SHOP", font="doh", width=180)  # creates artwork with the words]
welcome_message = """
*************************************************************************************************************************************
Welcome to Bruce Shoe store. You'll find a variety of men shoes kindly buy as many as possible cause you can never have enough shoes.
*************************************************************************************************************************************
"""
print(
    "___________________________________________________________________________________________________________________________")
print(colored(result, "blue"))
print(colored(welcome_message, "blue"))


def disp_menu():
    print("""
    Kindly select 0 to exit or the rest to execute the other operations:
        1. Customer Operations
        2. Products Operations
        3. Queries
        Q. To quite the program
    """)


def main_menu():
    while True:
        disp_menu()
        user_input = input("Please choose an option:\n")
        if user_input == "1":
            customeroperations.customer_operations()
        elif user_input == "2":
            productoperations.products_operations()
        elif user_input == "3":
            print("Welcome")
            break
        elif user_input.upper() == "Q":
            print("Exiting...........")
            print("See you next time")
            break
        else:
            print("Please enter a valid value in the range of 0 - 3")


main_menu()
