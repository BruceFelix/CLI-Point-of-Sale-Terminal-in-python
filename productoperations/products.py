# Imports
####################
import json
from customeroperations.customer import user_json_file
from customeroperations.customer import create_new_user
from customeroperations.customer import goods_bought

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


def check_user(customer):
    """
    Checks if a user exist or not.
    """
    users = user_json_file()
    # print(users)
    for (index, entry) in enumerate(users):
        if customer == entry["email"]:  # remember to use users input
            return index
        else:
            continue
    return False


def display_shoes():
    """
    Displays the shoes in store with their ids
    """
    print("What type of shoes do you need to buy?")
    shoes = products_json_file()
    for shoe_id, value in enumerate(shoes):
        print(f"For {value['name']} at {value['price']} - enter {shoe_id}")


def purchase_product():
    """
    Function used to purchase product.
    """
    users = user_json_file()
    shoes = products_json_file()
    customer = input("Please enter your email: \n")
    index = check_user(customer)
    if check_user(customer):
        cart = []
        while True:
            display_shoes()
            buyer_choice = input("Which shoe do you want?\n")
            pairs = input("How many pairs do you need?\n")
            cart.append([shoes[int(buyer_choice)]["name"], int(pairs), shoes[int(buyer_choice)]["price"], int(pairs) * int(shoes[int(buyer_choice)]["price"])])
            print("Do you want to continue shopping? ")
            print("* yes ")
            print("* no ")
            user_choice = input("")
            if user_choice.lower() == "yes":
                continue
            elif user_choice.lower() == "no":
                break
            else:
                print("Please choose valid answer.")
        print(cart)
        print(f"""
-------------------------------------------------
Customer Receipt
-------------------------------------------------
| Customer name: {users[int(index)]["name"]}
|           Products Bought
_________________________________________________
        """)
        print("""
| Product  Quantity     price        
        """)
        for i in cart:
            print(f"""
| {i[0]} - {i[1]}      : {i[2]}  each
            """)
        print(f"""
| Total purchase cost  : {cart[0][3]}
        """)
        total_goods_bought = 0
        # goods_sold(cart[0], cart[1])
        # goods_bought(cart[1], cart[2], users[int(index)]["email"])
        print(cart)

    else:
        print("The is no such user kindly register them first.")
        create_new_user()
        print("Thank you for registering you may proceed.")
        purchase_product()

purchase_product()


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
        elif operator_choice == "5":
            purchase_product()

        elif operator_choice == "6":
            pass
        elif operator_choice.upper() == "Q":
            break
        else:
            print("Please a valid option.")

# purchase_product()
# def something():
#     if buyer_choice == shoe_id:
#         pairs = input("How many do you want: ")
#         price = int(pairs) * int(shoes["price"])
#         print(price)
#         print(f"""
#             ---------------------------------------
#             Customer Receipt
#             ---------------------------------------
#             | Customer name : {users[int(index)]["name"]}
#             | Product bought: {shoes['name']}
#             | Total purchase: {price}
#             ---------------------------------------
#             Thank for shopping at Luku Shop
#             ---------------------------------------
#             """)
# # goods_bought(pairs, price, users[int(index)]['email'])