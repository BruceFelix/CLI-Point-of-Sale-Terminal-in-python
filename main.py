#IMPORTS
#####################
import pyfiglet
from termcolor import colored

#MAIN PROGRAM
##########

result = pyfiglet.figlet_format("LUKU SHOP", font = "doh", width= 180 ) # creates arwork with the words]
welcome_message ="""
*************************************************************************************************************************************
Welcome to Bruce Shoe store. You'll find a variety of men shoes kindly buy as many as possible cause you can never have enough shoes.
*************************************************************************************************************************************
"""
print("___________________________________________________________________________________________________________________________")
print(colored(result, "blue"))
print(colored(welcome_message, "blue"))



def disp_menu():
    print("""
    Kindly select 0 to exit or the rest to execute the other operations:
        1. Customer Operations
        2. Products Operations
        3. Queries
        0. To quite the program
    """)

while True:
    disp_menu()            
    user_input = input("Please choose an option:\n")
    if int(user_input) == 0:
        print("Exiting...........")
        print("See you next time")
        break
    elif int(user_input) == 1:
        print("Welcome")
        break
    elif int(user_input) == 2:
        print("Welcome")
        break
    elif int(user_input) == 3:
        print("Welcome")
        break
    else:
        print("Please enter a valid value in the range of 0 - 3")
        continue