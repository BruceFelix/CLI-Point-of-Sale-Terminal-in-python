# Imports
####################
import json

# Global variables
#####################
filename = "/home/cybernomand/Desktop/Desktop/Jenga School/SEPA/Sprint one/CLI-Point-of-Sale-Terminal-in-python/productoperations/products.json"


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
    with open(filename) as file:  # opens json file
        data = json.load(file)  # loads the data
    return data


def view_product():
    """
    Prints product data.
    """
    temp = products_json_file()
    i = 0
    for entry in temp:
        print(f"Product: {i} ", entry)
        i += 1


def create_new_product():
    """
    Adds a new product to the json file
    """
    with open(filename) as file:  # opens json file
        temp = json.load(file)  # loads the data
        temp.append(new_product())  # appends the data to the temporary variable
    with open(filename, "w") as f:
        json.dump(temp, f, indent=4)


def delete_product():
    """
    Deletes the selected product.
    """
    new_list_of_products = []
    view_product()  # prints user data
    data = products_json_file()  # loads user data from the json file
    data_length = len(data) - 1  # gets the total value of users in the json file
    print("Which product would you like to delete? \n")
    delete_product_option = input(f"Select a number 0 - {data_length}\n")
    i = 0
    for entry in data:
        if i == int(delete_product_option):
            pass
            # this part skips the part we want to delete and appends the rest to the file
            i += 1
        else:
            new_list_of_products.append(entry)  # creates a new file with the deleted intended user
            i += 1
    with open(filename, "w") as f:
        json.dump(new_list_of_products, f, indent=4)


def edit_product():
    """
    Edit the selected product.
    """
    new_list_of_products = []
    view_product()  # prints user data
    data = products_json_file()  # loads user data from the json file
    data_length = len(data) - 1  # gets the total value of users in the json file
    print("Which product would you like to update? \n")
    update_product_option = input(f"Select a number 0 - {data_length}\n")
    i = 0
    for entry in data:
        if i == int(update_product_option):
            """
            Takes the  selected user details and updates them to new values.
            """
            name = input("Enter the new name your want: \n")
            quantity = input("Enter the new quantity your want: \n")
            shoe_price = input("Enter the new price your want: \n")
            new_list_of_products.append({"name": name, "quantity": quantity, "price": shoe_price})
        else:
            new_list_of_products.append(entry)
            i += 1
    with open(filename, "w") as f:
        json.dump(new_list_of_products, f, indent=4)


def goods_sold(name, goods_sold):
    """
    Inputs the goods that the user has bought in the db.
    """
    updated_product_list = []
    product_details = products_json_file()
    for product in product_details:
        if name == product["name"]:
            name = product["name"]
            quantity = int(product["quantity"]) - int(goods_sold)
            price = product["price"]

            updated_product = {
                "name": name,
                "quantity": quantity,
                "price": price,
            }
            updated_product_list.append(updated_product)
        else:
            updated_product_list.append(product)
    with open(filename, "w") as f:
        json.dump(updated_product_list, f, indent=4)


def display_shoes():
    """
    Displays the shoes in store with their ids
    """
    print("What type of shoes do you need to buy?")
    shoes = products_json_file()
    for shoe_id, value in enumerate(shoes):
        print(f"For {value['name']} at {value['price']} - enter {shoe_id}")


def products_program():
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
        elif operator_choice.upper() == "Q":
            break
        else:
            print("Please a valid option.")
