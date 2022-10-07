#imports
######################
import json
# Global Vairable
#####################
filename = "database.json"

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

def loading_json_file_content():
    """
    Opens the json file and reads its content
    """
    with open(filename)  as file: #opens json file
        data = json.load(file) # loads the data
    return data

def view_data():
    """
    Prints User data.
    """
    temp = loading_json_file_content()
    i = 0
    for entry in temp:
        print(f"User:{i} ")
        print(entry)
        i += 1

def adding_new_data():
    """
    Adds a new user to the json file
    """
    with open(filename)  as file: #opens json file
        temp = json.load(file) # loads the data
        temp.append(new_customer()) # appends the data to the temporary variable
    with open (filename, "w") as f:
        json.dump(temp, f, indent=4)

def delete_user():
    """
    Deletes the selected user.
    """
    new_list_of_users = []
    view_data() # prints user data
    data = loading_json_file_content() # loads user data from the json file
    data_length = len(data) -1 # gets the total value of users in the json file
    print("Which user would you like to delete? \n")
    delete_user_option = input(f"Select a number 0 - {data_length}\n")
    i = 0
    for entry in data:
        if i == int(delete_user_option):
            pass
            i += 1
        else:
            new_list_of_users.append(entry)
            i +=1
    with open (filename, "w") as f:
        json.dump(new_list_of_users, f, indent=4)
delete_user()