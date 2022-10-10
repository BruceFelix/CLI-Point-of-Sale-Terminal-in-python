#Imports
####################
from itertools import product
import json
import sys
sys.path.append('/home/cybernomand/Desktop/Desktop/SEPA/Sprint one/CLI-Point-of-Sale-Terminal-in-python/customer/customer')
from  customer import user_json_file

#Global variables
#####################
filename = "products.json"


def product_operations():
    """
    Has the product operations.
    """
    print("Welcome to product operations.")
    print("Choose the operation you want to execute: ")
    print("\t1 To create New product.")
    print("\t2 To delete product.")
    print("\t3 To update product.")
    print("\t4 To view products in the system.")
    print("\t5 Buy product.")
    print("\t6 To go back to the main menu.")
    print("\tQ To quit the program.")

def new_product():
    """
    Capturing product details
    """
    product = {}
    print("Kindly enter the details of the new product: \n")
    # gets user details and adds them to the user dictionary.
    product["name"] = input("Name: ")
    product["quantity"] = input("Quantity: ")
    product["price"] = input("Selling price: ")
    return product
def products_json_file():
    """
    Opens the json file and reads its content
    """
    with open(filename)  as file: #opens json file
        data = json.load(file) # loads the data
    return data
def view_product():
    """
    Prints User data.
    """
    temp = products_json_file()
    i = 0
    for entry in temp:
        print(f"Product: {i} ")
        print(entry)
        i += 1
def create_new_product():
    """
    Adds a new product to the json file
    """
    with open(filename)  as file: #opens json file
        temp = json.load(file) # loads the data
        temp.append(new_product()) # appends the data to the temporary variable
    with open (filename, "w") as f:
        json.dump(temp, f, indent=4)
def delete_product():
    """
    Deletes the selected product.
    """
    new_list_of_products = []
    view_product() # prints user data
    data = products_json_file() # loads user data from the json file
    data_length = len(data) -1 # gets the total value of users in the json file
    print("Which product would you like to delete? \n")
    delete_product_option = input(f"Select a number 0 - {data_length}\n")
    i = 0
    for entry in data:
        if i == int(delete_product_option):
            pass
            # this part skips the part we want to delete and appends the rest to the file
            i += 1
        else:
            new_list_of_products.append(entry) #creates a new file with the deleted intended user
            i +=1
    with open (filename, "w") as f:
        json.dump(new_list_of_products, f, indent=4)
def edit_product():
    """
    Edit the selected user.
    """
    new_list_of_products = []
    view_product() # prints user data
    data = products_json_file() # loads user data from the json file
    data_length = len(data) -1 # gets the total value of users in the json file
    print("Which product would you like to update? \n")
    delete_product_option = input(f"Select a number 0 - {data_length}\n")
    i = 0
    for entry in data:
        if i == int(delete_product_option):
            """
            Takes the  selected user details and updates them to new values.
            """
            name = entry["name"]
            quantity = entry["quantity"]
            name = input("Enter the new name your want: \n")
            quantity = input("Enter the new quantity your want: \n")
            new_list_of_products.append({"name": name, "quantity" : quantity })
        else:
            new_list_of_products.append(entry)
            i +=1
    with open (filename, "w") as f:
        json.dump(new_list_of_products, f, indent=4)
def purchase_product():
    customer = input("Please enter your email: \n")
    users = user_json_file()
    print(users)

while True:
    """
    Displays user operations.
    """
    product_operations()
    operator_choice = input("Kindly choose an operation: \n")
    if operator_choice == "1":
        create_new_product()
    elif operator_choice == "2":
        delete_product()
    elif operator_choice == "3":
        edit_product()
    elif operator_choice == "4":
        view_product()
    elif operator_choice == "5":
        purchase_product()
    elif operator_choice == "6":
        pass
    elif operator_choice.upper() == "Q":
        break
    else:
        print("Please a valid option.")
# purchase_product()    

purch