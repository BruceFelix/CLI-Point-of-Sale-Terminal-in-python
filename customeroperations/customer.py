# imports
######################
import json
from validate_email import validate_email
import re
from termcolor import colored

# Global Variable
#####################

filename = "/home/cybernomand/Desktop/Desktop/Jenga School/SEPA/Sprint one/CLI-Point-of-Sale-Terminal-in-python/customeroperations/customerdb.json"


def customer_operations():
    """
    Has the customer operations.
    """
    print("Choose the operation you want to execute: ")
    print("\t1 To create New User.")
    print("\t2 To delete User.")
    print("\t3 To update User.")
    print("\t4 To view users in the system.")
    print("\t5 To search for a user in the system.")
    print("\tQ To return to the main program.")


def email_verifier():
    while True:
        email = input("Please enter a valid email address:\n ")
        if validate_email(email):
            return email
        else:
            continue


def phone_number_verifier():
    while True:
        number = input("Please enter a valid Kenyan phone number: \n")
        pattern = r"^(07|01)([0-9])(\d){7}$"
        if re.match(pattern, number):
            return number
            break
        else:
            continue


def new_customer():
    """
    Capturing user details
    """
    user = {}
    print("Kindly enter the details of the new customer: \n")
    # gets user details and adds them to the user dictionary.
    user["name"] = input("Name: ")
    user['email'] = email_verifier()
    user['number'] = phone_number_verifier()
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


def view_users():
    """
    Prints User data.
    """
    temp = user_json_file()
    i = 0
    print("\nThese are the users in the system")
    for entry in temp:
        print(f"User: {i} Name:", entry['name'], "Email:", entry['email'])
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


def search_user():
    """
    Checks if a user exist or not.
    """
    users = user_json_file()
    search_entry = input("Please enter the user's email:\n ")

    for (index, entry) in enumerate(users):
        if search_entry == entry["email"]:  # remember to use users input
            return colored((entry['name'] + " found!\n"), "green")
        else:
            continue
    return colored("User not registered!!\n", "red")


def delete_user():
    """
    Deletes the selected user.
    """
    new_list_of_users = []
    view_users()  # prints user data
    data = user_json_file()  # loads user data from the json file
    data_length = len(data) - 1  # gets the total value of users in the json file
    print("\nWhich user would you like to delete? \n")
    choice = input("""\n
If you wish to proceed enter yes:
To cancel enter no:    
    """)
    if choice.lower() == "yes":
        delete_user_option = input(f"Select a number 0 - {data_length}\n")
        i = 0
        for entry in data:
            if i == int(delete_user_option):
                print(colored((entry['name'], "has been deleted\n"), "red"))
                pass
                # this part skips the part we want to delete and appends the rest to the file
                i += 1
            else:
                new_list_of_users.append(entry)  # creates a new file with the deleted intended user
                i += 1
        with open(filename, "w") as f:
            json.dump(new_list_of_users, f, indent=4)
    elif choice.lower() == "no":
        print("Kindly proceed to the main menu")
        customer_program()


def edit_user():
    """
    Edit the selected user.
    """
    new_list_of_users = []
    view_users()  # prints user data
    data = user_json_file()  # loads user data from the json file
    data_length = len(data) - 1  # gets the total value of users in the json file
    print("Which user would you like to update? \n")
    choice = input("""
If you wish to proceed enter yes:
To cancel enter no:    
        \n""")
    if choice.lower() == "yes":
        delete_user_option = input(f"Select a number 0 - {data_length}\n")
        i = 0
        for entry in data:
            if i == int(delete_user_option):
                """
                Takes the  selected user details and updates them to new values.
                """
                name = input("Enter the new name your want: \n")
                email = email_verifier()
                number = phone_number_verifier()
                product = entry["products"]
                expenditure = entry["expenditure"]
                updated_user = {
                    "name": name,
                    "email": email,
                    "number": number,
                    "products": product,
                    "expenditure": expenditure
                }
                new_list_of_users.append(updated_user)
                print(colored("User updated! \n", "green"))
                i += 1
            else:
                new_list_of_users.append(entry)
                i += 1
        with open(filename, "w") as f:
            json.dump(new_list_of_users, f, indent=4)
    elif choice.lower() == "no":
        print("Kindly proceed to the main menu")
        customer_program()


def goods_bought(quantity, price, email):
    """
    Inputs the goods that the user has bought in the db.
    """
    updated_user_list = []
    user_details = user_json_file()
    for user in user_details:
        if email == user["email"]:
            name = user["name"]
            email = user["email"]
            number = user["number"]
            user['products'] = int(user["products"]) + int(quantity)
            user['expenditure'] = int(user['expenditure']) + int(price)
            updated_user = {
                "name": name,
                "email": email,
                "number": number,
                "products": user["products"],
                "expenditure": user["expenditure"]
            }
            updated_user_list.append(updated_user)
        else:
            updated_user_list.append(user)
    with open(filename, "w") as f:
        json.dump(updated_user_list, f, indent=4)


def customer_program():
    print(colored("Welcome to customer operations.\n", "green"))
    while True:
        """
        Displays user operations.
        """
        customer_operations()
        operator_choice = input("Kindly choose an operation: \n")
        if operator_choice == "1":
            create_new_user()
            print(colored("User created successfully!\n", "green"))
        elif operator_choice == "2":
            delete_user()
        elif operator_choice == "3":
            edit_user()
        elif operator_choice == "4":
            view_users()
            print("\n\n")
        elif operator_choice == "5":
            print(search_user())
        elif operator_choice.upper() == "Q":
            break
        else:
            print("Please a valid option.")
