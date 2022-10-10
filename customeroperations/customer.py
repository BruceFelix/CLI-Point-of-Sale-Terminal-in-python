# imports
######################
from ast import operator
import json
from tkinter import W

# Global Vairable
#####################
filename = "customerdb.json"


def customer_operations():
    """
    Has the customer operations.
    """
    print("Welcome to customer operations.")
    print("Choose the operation you want to execute: ")
    print("\t1 To create New User.")
    print("\t2 To delete User.")
    print("\t3 To update User.")
    print("\t4 To view users in the system.")
    print("\t5 To go back to the main menu.")
    print("\tQ To quit the program.")


def new_customer():
    """
    Capturing user details
    """
    user = {}
    print("Kindly enter the details of the new customer: \n")
    # gets user details and adds them to the user dictionary.
    user["name"] = input("Name: ")
    user["email"] = input("Email: ")
    user["number"] = input("Phone Number: ")
    user["products"] = 0
    user["expenditure"] = 0
    return user


def user_json_file():
    """
    Opens the json file and reads its content
    """
    with open(filename) as file:  # opens json file
        data = json.load(file)  # loads the data
    return data


def view_user():
    """
    Prints User data.
    """
    temp = user_json_file()
    i = 0
    for entry in temp:
        print(f"User: {i} ")
        print(entry)
        i += 1


def create_new_user():
    """
    Adds a new user to the json file
    """
    with open(filename) as file:  # opens json file
        temp = json.load(file)  # loads the data
        temp.append(new_customer())  # appends the data to the temporary variable
    with open(filename, "w") as f:
        json.dump(temp, f, indent=4)


def delete_user():
    """
    Deletes the selected user.
    """
    new_list_of_users = []
    view_user()  # prints user data
    data = user_json_file()  # loads user data from the json file
    data_length = len(data) - 1  # gets the total value of users in the json file
    print("Which user would you like to delete? \n")
    delete_user_option = input(f"Select a number 0 - {data_length}\n")
    i = 0
    for entry in data:
        if i == int(delete_user_option):
            pass
            # this part skips the part we want to delete and appends the rest to the file
            i += 1
        else:
            new_list_of_users.append(entry)  # creates a new file with the deleted intended user
            i += 1
    with open(filename, "w") as f:
        json.dump(new_list_of_users, f, indent=4)


def edit_user():
    """
    Edit the selected user.
    """
    new_list_of_users = []
    view_user()  # prints user data
    data = user_json_file()  # loads user data from the json file
    data_length = len(data) - 1  # gets the total value of users in the json file
    print("Which user would you like to update? \n")
    delete_user_option = input(f"Select a number 0 - {data_length}\n")
    i = 0
    for entry in data:
        if i == int(delete_user_option):
            """
            Takes the  selected user details and updates them to new values.
            """
            name = entry["name"]
            email = entry["email"]
            number = entry["number"]
            name = input("Enter the new name your want: \n")
            email = input("Enter the new email your want: \n")
            number = input("Enter the new number your want: \n")
            new_list_of_users.append({"name": name, "email": email, "number": number})
        else:
            new_list_of_users.append(entry)
            i += 1
    with open(filename, "w") as f:
        json.dump(new_list_of_users, f, indent=4)


while True:
    """
    Displays user operations.
    """
    customer_operations()
    operator_choice = input("Kindly choose an operation: \n")
    if operator_choice == "1":
        create_new_user()
    elif operator_choice == "2":
        delete_user()
    elif operator_choice == "3":
        edit_user()
    elif operator_choice == "4":
        view_user()
    elif operator_choice == "5":
        pass
    elif operator_choice.upper() == "Q":
        break
    else:
        print("Please a valid option.")
